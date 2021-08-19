class Solution:

    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        memo = {}

        def cost(i, j):
            r = 0
            while i < j:
                if s[i] != s[j]:
                    r += 1
                i += 1
                j -= 1
            return r

        def divide(st, d):
            if (st, d) in memo:
                return memo[st, d]
            if d == n - st:
                return 0
            if d == 1:
                return cost(st, n - 1)
            ans = float('inf')
            for i in range(st + 1, n - d + 2):
                ans = min(ans, cost(st, i - 1) + divide(i, d - 1))
            memo[st, d] = ans
            return ans
        return divide(0, k)
