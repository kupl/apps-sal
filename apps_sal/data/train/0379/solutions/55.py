class Solution:

    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        N = len(nums1)
        M = len(nums2)

        def get_pos(nums):
            pos = defaultdict(lambda: -1)
            for (i, x) in enumerate(nums):
                pos[x] = i
            return pos
        pos1 = get_pos(nums1)
        pos2 = get_pos(nums2)
        dp1 = [0] * (N + 1)
        dp2 = [0] * (M + 1)
        (i, j) = (N - 1, M - 1)
        while i >= 0 or j >= 0:
            while i >= 0 and pos2[nums1[i]] < 0:
                dp1[i] = nums1[i] + dp1[i + 1]
                i -= 1
            while j >= 0 and pos1[nums2[j]] < 0:
                dp2[j] = nums2[j] + dp2[j + 1]
                j -= 1
            if i >= 0:
                p = pos2[nums1[i]]
                dp1[i] = nums1[i] + max(dp1[i + 1], dp2[p + 1])
                i -= 1
            if j >= 0:
                p = pos1[nums2[j]]
                dp2[j] = nums2[j] + max(dp2[j + 1], dp1[p + 1])
                j -= 1
        res = max(dp1[0], dp2[0])
        return res % (10 ** 9 + 7)
