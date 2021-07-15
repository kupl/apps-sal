class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        counter = [0]*121
        res = 0
        for a in ages:
            if a<=14: continue
            counter[a] += 1
            
        for i in range(15, 121):
            for j in range(i+1):
                if j<=0.5*i+7: continue
                res += counter[i]*counter[j]
                
                if i==j:
                    res -= counter[i]
                    
        return res
