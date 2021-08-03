class Solution:
    def numWays(self, s: str) -> int:
        ones = s.count('1')
        if ones % 3 != 0:
            return 0
        n = len(s)
        mod = 10**9 + 7
        if ones == 0:
            return (n - 1) * (n - 2) // 2 % mod
        count = 0
        first_count = 0
        second_count = 0
        for cha in s:
            if cha == '1':
                count += 1
            if count == ones // 3:
                first_count += 1
            elif count == ones // 3 * 2:
                second_count += 1
        return first_count * second_count % mod
