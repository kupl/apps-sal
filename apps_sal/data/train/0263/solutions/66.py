move_map = {
    0: {4,6},
    1: {6,8},
    2: {7,9},
    3: {4,8},
    4: {3, 9, 0},
    5: {},
    6: {1, 0, 7},
    7: {2, 6},
    8: {1, 3},
    9: {2, 4}
}

class Solution:    
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        old_row = [1 for _ in move_map]
        new_row = [0 for _ in move_map]
        for N in range(2,n+1):
            for key in move_map:
                res = 0
                for new_key in move_map[key]:
                    res += old_row[new_key]
                new_row[key] = res
            for idx, n in enumerate(new_row):
                old_row[idx] = n
                
        return sum(new_row) % (10**9 + 7)
