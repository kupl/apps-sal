class Solution:

    def numTilePossibilities(self, tiles: str) -> int:
        seen = set()
        ans = set()

        def backtrack(tiles, seen, curr):
            if curr != '' and curr not in ans:
                ans.add(curr)
            for i in range(len(tiles)):
                if i not in seen:
                    seen.add(i)
                    backtrack(tiles, seen, curr + tiles[i])
                    seen.remove(i)
        backtrack(tiles, seen, '')
        return len(ans)
