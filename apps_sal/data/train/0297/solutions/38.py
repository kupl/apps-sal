class Solution:
    def numTilePossibilities(self, tiles: str) -> int:

        
        def recur(tiles):
            if not tiles: return set()
            ans = set()
            temp = ''
            while tiles:
                v = tiles[0]
                ans.add(v)
                new = recur(temp+tiles[1:])
                ans.update(new)
                for k in new: ans.add(v+k)
                temp+=tiles[0]
                tiles = tiles[1:]
            return ans
            
        ans = recur(tiles)
        # print(ans)
        return len(ans)
