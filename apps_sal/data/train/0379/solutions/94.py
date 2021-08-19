class Solution:

    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        common = set(nums1).intersection(set(nums2))
        segments1 = []
        tmp = 0
        for i in nums1:
            tmp += i
            if i in common:
                segments1.append(tmp)
                tmp = 0
        segments1.append(tmp)
        segments2 = []
        tmp = 0
        for i in nums2:
            tmp += i
            if i in common:
                segments2.append(tmp)
                tmp = 0
        segments2.append(tmp)
        ans = 0
        for i in range(len(segments1)):
            ans += max(segments1[i], segments2[i])
        return ans % (10 ** 9 + 7)
