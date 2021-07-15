class Solution:
    def stone_game(self, memo, n):
        if n in memo:
            return memo[n]
        
        memo[n] = False
        for cand in range(1, int(math.sqrt(n)) + 1):
            i = cand * cand
            memo[n] = memo[n] or not self.stone_game(memo, n-i)
            if memo[n]:
                return True
        
        return memo[n]
    
                
    def winnerSquareGame(self, n: int) -> bool:
        '''
        - implementation 
        '''
        can_i_win = defaultdict(bool)
        
        can_i_win[1] = True
        can_i_win[0] = False
        self.stone_game(can_i_win, n)
        
        return can_i_win[n]
