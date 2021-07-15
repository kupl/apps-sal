class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        count = 0
        
        counter = [0]*121
        for i in ages:
            counter[i] += 1
        
        for a in range(1, 121):
            for b in range(1, 121):
                if b > a:
                    continue
                
                if b <= 0.5*a+7:
                    continue
                
                if b > 100 and a < 100:
                    continue
                
                count += counter[a]*counter[b]
                
                if a == b:
                    count -= counter[a]
        
        return count
