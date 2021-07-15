from functools import lru_cache
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        a = rating
        @lru_cache()
        def helper(curr, left):
            if left == 0: return 1
            if curr == len(a): return 0
            
            return sum([helper(i, left-1) for i in range(curr+1, len(a)) if a[i] > a[curr]] +[0])
        
        res = sum([helper(i, 2) for i in range(len(a))]+[0])
        helper.cache_clear()
        a = a[::-1]
        res += sum([helper(i, 2) for i in range(len(a))]+[0])
        return res
