class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        
        
        '''
        https://leetcode.com/problems/dice-roll-simulation/discuss/403756/Java-Share-my-DP-solution
        
        num[i,j] = num sequences with i rolls that ends with j
        
        num[i,j] = sum_{k≠j} (num[i-1,k]) + num[i-1,j] - num[i-rollMax[i],j]
        '''
        
        num = [[1]*6+[6] for i in range(16)]  # rollMax[i] <= 15
        pointer = 1
        
        def idxLast(i):
            return (pointer - i) % 16
        
        for k in range(2,n+1):
            
            for j in range(6):
                
                if rollMax[j] >= k:
                    num[idxLast(0)][j] = num[idxLast(1)][-1]
                
                else:
                    num[idxLast(0)][j] = 0
                    for i in range(1, rollMax[j]+1):
                        num[idxLast(0)][j] = (num[idxLast(0)][j] + num[idxLast(i)][-1] - num[idxLast(i)][j]) % int(1E9 + 7)
            
            num[idxLast(0)][-1] = sum(num[idxLast(0)][:6]) % int(1E9 + 7)
            
            pointer += 1
        
        # print(num)
        
        return num[idxLast(1)][-1] % int(1E9 + 7)

