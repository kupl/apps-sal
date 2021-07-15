class Solution:
    def numTeams(self, rating: List[int]) -> int:
        
        
        def backtrack(rating, cur, index):
            
            if len(cur) == 3:
                self.count += 1
                return
            
            if len(cur) > 3:
                return
            
            for i in range(index, len(rating)):
                if len(cur) == 2 and cur[0] < cur[1] and rating[i] < cur[1]:
                    continue
                if len(cur) == 2 and cur[0] > cur[1] and rating[i] > cur[1]:
                    continue
                    
                backtrack(rating, cur + [rating[i]], i + 1)
        
        
        self.count = 0
        backtrack(rating, [], 0)
        return self.count
