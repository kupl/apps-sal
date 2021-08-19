class Solution:

    def numTilePossibilities(self, tiles: str) -> int:
        tiles = ''.join(sorted(tiles))
        memo = {}

        def helper(s, k):
            if (s, k) not in memo:
                if k == 0:
                    memo[s, k] = 1
                else:
                    (last, ans) = ('', 0)
                    for i in range(len(s)):
                        if s[i] != last:
                            last = s[i]
                            ans += helper(s[:i] + s[i + 1:], k - 1)
                    memo[s, k] = ans
            return memo[s, k]
        ret = 0
        for k in range(1, len(tiles) + 1):
            ret += helper(tiles, k)
        return ret
