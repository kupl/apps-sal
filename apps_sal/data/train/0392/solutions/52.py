class Solution:
    def numWays(self, s: str) -> int:
        n = len(s)
        count = 0
        cur = 0
        mod = 1000000007
        for i in range(len(s)):
            if s[i] == '1':
                cur += 1

        if cur == 0:
            return (((n - 1) * (n - 2)) // 2) % mod

        left = 0
        lc = 0
        for i in range(n):
            if s[i] == '1':
                left += 1
            if left == cur / 3:
                lc += 1
            if left > cur / 3:
                break
        right = 0
        rc = 0
        for i in range(n - 1, -1, -1):
            if s[i] == '1':
                right += 1
            if right == cur / 3:
                rc += 1
            if right > cur / 3:
                break
        return (lc * rc) % mod
