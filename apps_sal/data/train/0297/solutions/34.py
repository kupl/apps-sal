class Solution:

    def numTilePossibilities(self, tiles):
        res = set()

        def helper(t, curr, k):
            if k == len(curr):
                res.add(curr)
                return
            for i in range(len(t)):
                helper(t[:i] + t[i + 1:], curr + t[i], k)
        for i in range(1, len(tiles) + 1):
            helper(tiles, '', i)
        return len(res)
