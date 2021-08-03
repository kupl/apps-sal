class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:

        n = len(arr)

        mem = {}

        def dp(i, j):
            if i == j:
                return (0, arr[i])
            if i == j - 1:
                return (arr[i] * arr[j], max(arr[i], arr[j]))
            else:
                if (i, j) in mem:
                    return mem[(i, j)]
                pp = max(arr[i:j + 1])
                minn = 1e10
                for k in range(i, j):
                    l, lm = dp(i, k)
                    r, rm = dp(k + 1, j)
                    minn = min(minn, l + r + lm * rm)
                mem[(i, j)] = (minn, pp)
                return mem[(i, j)]

        return dp(0, n - 1)[0]
