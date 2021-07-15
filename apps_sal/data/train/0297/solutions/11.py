class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        d = {}
        for i in range(len(tiles)):
            if (tiles[i] in d):
                d[tiles[i]] += 1
            else:
                d[tiles[i]] = 1
        def countnum(d):
            if (d == {}):
                return 0
            c = 0
            s = set(d.items())
            for k, v in s:
                d[k] -= 1
                if (d[k] == 0):
                    del(d[k])
                c += 1 + countnum(d)
                if (k in d):
                    d[k] += 1
                else:
                    d[k] = 1
            return c
        return countnum(d)
                
        

