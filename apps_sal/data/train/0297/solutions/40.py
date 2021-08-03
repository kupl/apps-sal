class Solution:
    def numTilePossibilities(self, tiles: str) -> int:

        def recur(tiles):
            if not tiles:
                return set()
            ans = set()
            for i, v in enumerate(tiles):
                ans.add(v)
                new = recur(tiles[:i] + tiles[i + 1:])
                ans.update(new)
                for k in new:
                    ans.add(v + k)
            return ans

        ans = recur(tiles)
        # print(ans)
        return len(ans)
