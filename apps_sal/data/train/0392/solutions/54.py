class Solution:
    def numWays(self, s: str) -> int:
        one, n, m = s.count('1'), len(s), 10**9 + 7
        # special case: first one for left -> n-2, first two for left -> n-3, ..., 2, 1
        # -> (n-2) + (n-3) + ... + 2 + 1 -> (n-1) * (n-2) // 2
        if not one:
            return (n - 1) * (n - 2) // 2 % m
        if one % 3:
            return 0
        curr = l = r = 0
        for c in s:
            curr += c == '1'
            l += curr == (one // 3)
            r += curr == (2 * one // 3)

        return l * r % m
