class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        faces = len(rollMax)
        
        d = [[0] * (faces + 1) for _ in range(n+1)]
        
        d[0][faces] = 1
        
        for i in range(faces):
            d[1][i] = 1
            
        d[1][faces] = sum(d[1])
        
        for i in range(2, n + 1):
            for j in range(faces):
                for k in range(1, rollMax[j] + 1):  
                    if i - k < 0:
                        break
                        
                    d[i][j] += d[i-k][faces] - d[i-k][j]
            d[i][faces] = sum(d[i])
            
        #for i in range(n+1):
        #    print(d[i])
                    
        return d[n][faces] % (10**9+7)
