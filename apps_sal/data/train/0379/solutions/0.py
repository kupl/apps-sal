class Solution:

    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        d2 = {nums2[i]: i for i in range(len(nums2))}
        _nums1 = []
        _nums2 = []
        (prev_i, prev_j) = (0, 0)
        for i in range(len(nums1)):
            if nums1[i] in d2:
                _nums1.append(sum(nums1[prev_i:i]))
                _nums2.append(sum(nums2[prev_j:d2[nums1[i]]]))
                _nums1.append(nums1[i])
                _nums2.append(nums1[i])
                prev_i = i + 1
                prev_j = d2[nums1[i]] + 1
        _nums1.append(sum(nums1[prev_i:]))
        _nums2.append(sum(nums2[prev_j:]))
        print(_nums1)
        print(_nums2)
        n = len(_nums1)
        ans = 0
        for i in range(n):
            ans += max(_nums1[i], _nums2[i])
        return ans % (10 ** 9 + 7)
