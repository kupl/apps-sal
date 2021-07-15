class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [1 for _ in range(10)]
        
        move = [[4,6], [6,8], [7,9], [4,8], [3,9,0], [], [1,7,0], [2,6], [1,3], [4,2]]
        for i in range(n-1):
            dp2 = [0] *10
            for node, count in enumerate(dp):
                for nei in move[node]:
                    dp2[nei] += count
                    dp2[nei] %MOD
            dp = dp2
        print(dp)
        return sum(dp)%MOD
