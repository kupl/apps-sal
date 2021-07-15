class Solution:
    def knightDialer(self, n: int) -> int:
        def get_position(pos):
            _map= {0: [4, 6],
                    1: [8, 6],
                    2: [7, 9],
                    3: [4, 8],
                    4: [3, 9, 0],
                    5: [],
                    6: [1,7,0],
                    7: [2,6],
                    8: [1,3],
                    9: [4,2],
                   }
            return _map[pos]
        cache = {}
        def solve(pos, step):
            key = (pos, step)
            if key not in cache:
                if step>=n:
                    return 1
                res = 0
                for i in get_position(pos):
                    res += solve(i, step + 1)
                    res = res % (pow(10,9)  + 7)
                cache[key] = res
            return cache[key]
        res = 0
        
        for i in range(0, 10):
            res += solve(i, 1)
        return res % (pow(10,9)  + 7)
