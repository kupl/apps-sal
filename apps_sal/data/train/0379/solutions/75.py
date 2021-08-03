class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        matrix = []
        matrix.append(nums1[:])
        matrix.append(nums2[:])
        dics = []
        dics.append({num: i for i, num in enumerate(nums1)})
        dics.append({num: i for i, num in enumerate(nums2)})
        sys.setrecursionlimit(10**6)

        @lru_cache(None)
        def dfs(row, index):
            if index >= len(matrix[row]):
                return 0
            cur = matrix[row][index]
            res = cur + dfs(row, index + 1)
            if cur in dics[1 - row]:
                res = max(res, cur + dfs(1 - row, dics[1 - row][cur] + 1))
            return res
        mod = 10 ** 9 + 7
        return max(dfs(0, 0), dfs(1, 0)) % mod
