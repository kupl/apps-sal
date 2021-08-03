class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        target1 = {}
        target2 = {}

        for i in range(len(nums1)):
            for j in range(i + 1, len(nums1)):
                v = nums1[i] * nums1[j]
                if v in target1:
                    target1[v] += 1
                else:
                    target1[v] = 1

        for i in range(len(nums2)):
            for j in range(i + 1, len(nums2)):
                v = nums2[i] * nums2[j]
                if v in target2:
                    target2[v] += 1
                else:
                    target2[v] = 1

        answer = 0
        print(target1, target2)
        for num in nums1:
            if num * num in target2:
                answer += target2[num * num]
        for num in nums2:
            if num * num in target1:
                answer += target1[num * num]

        return answer
