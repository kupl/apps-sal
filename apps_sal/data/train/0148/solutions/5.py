class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        
        temp = sorted( zip(difficulty, profit) )
        
        d = collections.defaultdict(int)
        
        for u, v in temp:
            d[u] = v
        
        maxdifficulty = max(worker)
        
        for i in range(1, maxdifficulty + 1):
            d[i] = max(d[i], d[i - 1])
            
        # print (d)
            
        ans = 0
        
        for i in worker:
            
            # print (i, d[i])
            
            ans += d[i]
            
        return ans
                
        
        
        
        
        
        

