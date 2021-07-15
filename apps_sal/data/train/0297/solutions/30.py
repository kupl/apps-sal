class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def solve(s,visited):
            seen.add(s)
            if len(s) == len(tiles):return 0
            for i , v in enumerate(tiles):
                if i not in visited:
                    solve(s + v,visited | {i})
            return len(seen)
        seen = set()
        return solve('',set()) - 1

