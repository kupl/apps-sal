class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        set2 = set(arr2)
        arr2 = sorted(set2)
        N, M = len(arr1), len(arr2)
        to_index = {}
        left = 0
        for x in sorted(arr1):
            while left < M and arr2[left] <= x:
                left += 1
            to_index[x] = left - 1 if left < M else M

        print(to_index, arr2)
        dp = [[[None, None] for _ in range(M + 1)] for _ in range(N)]

        def solve(i, j, k):
            if i == N: return 0
            if j > M or (j == M and k == 1): return N + 1
            if dp[i][j][k] is None:
                if i == 0:
                    dp[i][j][k] = min(solve(i + 1, to_index[arr1[0]], 0), 1 + solve(i + 1, 0, 1))
                else:
                    result = N + 1
                    if j < M - 1:
                        result = 1 + solve(i + 1, j + 1, 1)
                    if k == 0 and arr1[i] > arr1[i - 1]:
                        result = min(result, solve(i + 1, to_index[arr1[i]], 0))
                    if k == 1 and arr1[i] > arr2[j]:
                        result = min(result, solve(i + 1, to_index[arr1[i]], 0))
                    dp[i][j][k] = result
            return dp[i][j][k]
        result = solve(0, 0, 0)
        # for i in range(N):
        #     for j in range(M):
        #         for k in [0, 1]:
        #             print(dp[i][j][k], i, j, k)
        return result if result <= N else -1
