class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        memo = {1: 0}  # Exit Condition Stored in Memory

        def power(x):
            if x in memo:
                return memo[x]
            n = memo[x] = 1 + power((3 * x + 1) if x & 1 else (x >> 1))
            return n
        ans = [(x, power(x)) for x in range(lo, hi + 1)]
        sorted_ans = sorted(ans, key=lambda t: t[1])
        return sorted_ans[k - 1][0]
