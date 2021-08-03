class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        l1, l2 = len(nums1), len(nums2)
        g = defaultdict(set)
        for i in range(1, l1):
            g[nums1[i - 1]].add(nums1[i])
        for i in range(1, l2):
            g[nums2[i - 1]].add(nums2[i])

        @lru_cache(None)
        def dfs(n):
            x = 0
            for i in g[n]:
                x = max(x, dfs(i))
            return n + x
        res = max(dfs(nums1[0]), dfs(nums2[0]))
        return res % 1000000007
