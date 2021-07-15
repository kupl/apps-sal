from functools import lru_cache
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}
        return self.dfs(0, 0, piles, 0, len(piles)-1, memo)
    
    def dfs(self, person1, person2, piles, start, end, memo):
        if (person1, person2, start, end) in memo:
            return memo[(person1, person2, start, end)]
        
        if end-start == 1:
            if person1 + max(piles) > person2 + min(piles):
                return True
            else:
                return False
        
        case1_person1 = person1 + piles[0]
        res1 = self.dfs(person2, case1_person1, piles, start+1, end, memo)
        if res1 == False:
            memo[(person1, person2, start, end)] = True
            return True
        
        case2_person1 = person1+piles[-1]
        res2 = self.dfs(person2, case2_person1, piles, start, end-1, memo)
        if res2 == False:
            memo[(person1, person2, start, end)] = True
            return True
        

        memo[(person1, person2, start, end)] = False
        
        return False
    

