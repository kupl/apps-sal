class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        from heapq import heappush, heappop
        R, C = len(grid), len(grid[0])
        start = None
        K = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == '@':
                    start = (r, c)
                elif grid[r][c].isupper():
                    K = max(K, ord(grid[r][c]) - ord('A') + 1)
        
        assert start is not None
        assert K > 0
        
        h = [(0, *start, 0)]
        seen = set()
        while h:
            m, r, c, keys = heappop(h)
            if (r, c, keys) in seen:
                continue
            seen.add((r, c, keys))
            if keys == (1 << K) - 1:
                return m
            for rp, cp in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                if 0 <= rp < R and 0 <= cp < C:
                    char = grid[rp][cp]
                    if char == '#' or char.isupper() and keys & (1 << (ord(char) - ord('A'))) == 0:
                        continue
                    new_keys = keys
                    if char.islower():
                        new_keys |= (1 << (ord(char) - ord('a')))
                    heappush(h, (m+1, rp, cp, new_keys))
        return -1
                        
                        
                        

