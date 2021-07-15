class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        memo, mod = [[0]*6 for _ in range(n)], 10**9+7
        memo[0] = [1]*6
        
        for i in range(1,n):
            prev_sum = sum(memo[i-1]) % mod
            for j in range(6):
                memo[i][j] = prev_sum
                if i == rollMax[j]:
                    memo[i][j] -= 1
                elif i > rollMax[j]:
                    memo[i][j] = (memo[i][j] - sum(memo[i-rollMax[j]-1]) + memo[i-rollMax[j]-1][j]) % mod
                
        return sum(memo[n-1]) % mod
