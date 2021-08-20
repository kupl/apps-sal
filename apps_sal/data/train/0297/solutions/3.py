class Solution:

    def numTilePossibilities(self, tiles: str) -> int:

        @lru_cache(None)
        def find(s):
            if len(s) <= 1:
                return set([s])
            ret = set()
            for i in range(len(s)):
                head = s[i]
                tails = find(s[:i] + s[i + 1:])
                ret = ret.union(tails)
                for tail in tails:
                    for j in range(len(tail) + 1):
                        temp = tail[:j] + head + tail[j:]
                        ret.add(temp)
            return ret
        res = find(tiles)
        return len(set(res))
