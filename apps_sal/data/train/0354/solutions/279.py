class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        
        Q = [[0 for j in range(7)] for i in range(n+1)]
        Q[0][-1]=1
        MAX = 10**9+7
        for i in range(1,n+1):
            for j in range(6):
                if i<=rollMax[j]:
                    Q[i][j] = Q[i-1][-1]
                else:
                    for k in range(rollMax[j]):
                        Q[i][j]=(Q[i][j]%MAX+(Q[i-k-1][-1]-Q[i-k-1][j])%MAX)%MAX
                Q[i][-1]=(Q[i][-1]%MAX+Q[i][j]%MAX)%MAX
        return Q[-1][-1]
