class Solution:
    def numWays(self, s: str) -> int:
        n, ones = len(s), []
        for i, val in enumerate(s):
            if val == '1':
                ones.append(i)

        target = len(ones)
        if target == 0:
            return (((n - 1) * (n - 2)) // 2) % (10**9 + 7)

        if target % 3 != 0:
            return 0

        c = target // 3
        return ((ones[c] - ones[c - 1]) * (ones[2 * c] - ones[2 * c - 1])) % (10**9 + 7)
