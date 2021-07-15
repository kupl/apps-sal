class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        t = [[0]*(K+1) for _ in range(N+1)]
        for i in range(1,N+1):
            for j in range(1,K+1):
                t[i][j] = t[i-1][j] + t[i-1][j-1] + 1
                
            if t[i][j] >= N:
                return i
