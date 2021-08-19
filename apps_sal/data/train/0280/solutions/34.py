class Solution:

    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        memo = dict()
        cost_memo = dict()

        def find_cost(l, r):
            (a, b) = (l, r)
            if (l, r) not in memo:
                cost = 0
                while l < r:
                    cost += s[l] != s[r]
                    l += 1
                    r -= 1
                cost_memo[a, b] = cost
            return cost_memo[a, b]

        def top_down(i, k):
            if n - i == 1:
                return 0
            if k == 1:
                return find_cost(i, n - 1)
            if (i, k) not in memo:
                res = float('inf')
                for j in range(i + 1, n - k + 2):
                    res = min(res, find_cost(i, j - 1) + top_down(j, k - 1))
                memo[i, k] = res
            return memo[i, k]
        return top_down(0, k)
