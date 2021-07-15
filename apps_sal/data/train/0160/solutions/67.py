class Solution:
    # return True would work because Alex always wins the game
    def stoneGame(self, piles: List[int]) -> bool:
        prefix = list(itertools.accumulate(piles))
        
        @lru_cache(maxsize=None)
        def getScore(i, j):
            if i > j:
                return 0
            
            stones = float('-inf')
            prev = prefix[i - 1] if i - 1 >= 0 else 0
            stones = max(stones, prefix[j] - prev - getScore(i + 1, j))
            stones = max(stones, prefix[j] - prev - getScore(i, j - 1))
            return stones
            
        alex_score = getScore(0, len(piles) - 1)
        if alex_score > prefix[-1] - alex_score:
            return True
        return False
