class Solution:
    def numTilePossibilities(self, tiles):
        res = set()

        def helper(t, curr, k):
            if k == len(curr):
                res.add(curr)
                return  # return so that the loop below doesn't continue when you meet the length requirement

            for i in range(len(t)):
                # call helper with everything but the current value
                helper(t[:i] + t[i + 1:], curr + t[i], k)

        # start at size 1 and move until size len(tiles), +1 because range doesn't include the endpoint
        for i in range(1, len(tiles) + 1):
            helper(tiles, '', i)

        return((len(res)))
