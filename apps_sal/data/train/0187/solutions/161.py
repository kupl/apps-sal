class Solution:
    def minOperationsMaxProfit(self, c: List[int], b: int, r: int) -> int:
        n = len(c)
        i = 0
        rest = 0
        max_val, max_i = 0, -2
        val = 0
        while i < n or rest > 0:
            if i < n:
                rest += c[i]
            p = min(rest, 4)
            val += p * b - r
            if val > max_val:
                max_val = val
                max_i = i
            rest -= p
            i += 1
        return max_i + 1
