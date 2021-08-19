class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        lookup1 = dict()
        lookup2 = dict()
        for num1 in nums1:
            lookup1[num1] = lookup1.get(num1, 0) + 1
        for num2 in nums2:
            lookup2[num2] = lookup2.get(num2, 0) + 1
        mem = dict()

        ans = 0
        ans1 = 0
        ans2 = 0
        for idx1 in range(len(nums1)):
            num1 = nums1[idx1]
            if num1 in mem:
                ans1 += mem[num1][0]
                ans2 += mem[num1][1]
                continue
            lookup1[num1] -= 1
            ans1_tmp = 0
            ans2_tmp = 0
            for idx2 in range(len(nums2)):
                num2 = nums2[idx2]
                lookup2[num2] -= 1
                if lookup2.get((num1**2 / num2), 0) > 0:
                    #print(num1, num2, lookup2)
                    ans1_tmp += lookup2[(num1**2 / num2)]
                lookup2[num2] += 1

                if lookup1.get((num2**2 / num1), 0) > 0:
                    ans2_tmp += lookup1[(num2**2 / num1)]
            mem[nums1[idx1]] = (ans1_tmp, ans2_tmp)
            ans1 += ans1_tmp
            ans2 += ans2_tmp

            lookup1[num1] += 1

        return ans1 // 2 + ans2 // 2
