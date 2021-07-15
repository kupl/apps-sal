class Solution:
    def numTeams(self, rating: List[int]) -> int:
        
        if len(rating) < 3:
            return 0
        
        from functools import lru_cache
        @lru_cache(maxsize = None)
        def bt(start, lastVal, countAdded, sign):
            if countAdded == 3:
                return 1
            
            if start == len(rating):
                return 0
            
            totalCount = 0
            for i in range(start, len(rating)):
                if lastVal*sign < rating[i]*sign:
                    totalCount += bt(i + 1, rating[i], countAdded + 1, sign)
            return totalCount
        
        return bt(0, 0, 0, 1) + bt(0, float('inf'), 0, -1)

