class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:

        n = len(arr)
        maxs = [[0 if i != j else arr[i] for j in range(n)] for i in range(n)]

        for i in range(n - 1):
            for j in range(i + 1, n):
                for k in range(i, j):
                    maxs[i][j] = max(maxs[i][k], maxs[k + 1][j])
                    maxs[j][i] = maxs[i][j]

        print(maxs)

        ans = [[0 for j in range(n)] for i in range(n)]

        for l in range(1, n):
            for i in range(n - l):
                j = l + i
                print((i, j))
                ans[i][j] = min(maxs[i][k] * maxs[k + 1][j] + ans[i][k] + ans[k + 1][j] if j - i > 1 else maxs[i][k] * maxs[k + 1][j] for k in range(i, j))

        print(ans)

        return ans[0][n - 1]
