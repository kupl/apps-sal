class Solution:
    def knightDialer(self, n: int) -> int:
#         MOD = 10**9 + 7
#         moves = [[4,6],[6,8],[7,9],[4,8],[3,9,0],[],
#                      [1,7,0],[2,6],[1,3],[2,4]]

#         dp = [1] * 10
#         for hops in range(n-1):
#             dp2 = [0] * 10
#             for node, count in enumerate(dp):
#                 for nei in moves[node]:
#                     dp2[nei] += count
#                     dp2[nei] %= MOD
#             dp = dp2
#         return sum(dp) % MOD
        modulo = pow(10,9)  + 7
        get_position= [[4,6],[6,8],[7,9],[4,8],[3,9,0],[],
                     [1,7,0],[2,6],[1,3],[2,4]]   
        cache = {}
        def solve(pos, step):
            key = (pos, step)
            if key not in cache:
                if step>=n:
                    return 1
                res = 0
                for i in get_position[pos]:
                    res += solve(i, step + 1)
                    res = res % modulo
                cache[key] = res
            return cache[key]
        res = 0
        
        for i in range(10):
            res += solve(i, 1)
        return res % modulo
