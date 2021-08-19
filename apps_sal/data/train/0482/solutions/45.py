class Solution:

    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[float('inf') for i in range(n)] for j in range(n)]
        mem = {}
        m = [[-float('inf') for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(i, n):
                if i == j:
                    m[i][j] = arr[i]
                    continue
                for k in range(i, j + 1):
                    m[i][j] = max(m[i][j], arr[k])

        def rec(left, right):
            if right - left == 0:
                return 0
            elif (left, right) in mem:
                return mem[left, right]
            else:
                ans = float('inf')
                for k in range(left, right):
                    ans = min(ans, rec(left, k) + rec(k + 1, right) + m[left][k] * m[k + 1][right])
                mem[left, right] = ans
                return ans
        return rec(0, n - 1)
