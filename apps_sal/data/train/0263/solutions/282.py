class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        if n == 1:
            return 10
        moves = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }
        
        memo = dict()
        
        def count_moves(position, digits):
            if digits == 1:
                return 1
            if (position, digits) in memo:
                return memo[position, digits]
            curr = 0
            for m in moves[position]:
                curr += count_moves(m, digits - 1)
            memo[position, digits] = curr % MOD
            return memo[position, digits]
        
        res = 0
        
        for pos in moves.keys():
            res += count_moves(pos, n)
            res %= MOD
            
        return res
