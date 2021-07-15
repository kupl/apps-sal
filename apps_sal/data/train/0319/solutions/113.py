class Solution:
    def stoneGameIII(self, stoneValue) -> str:
        total_value = sum(stoneValue)
        num_stones = len(stoneValue)
        
        @lru_cache(None)
        def helper(ind, player):
            if ind >= num_stones:
                return 0
            
            if player == 'A': # Alex as the player
                tmp_result = []
                for i in range(1, 4):
                    if ind + i <= num_stones:
                        tmp_result.append( sum(stoneValue[ind: ind+i]) + helper(ind+i, 'L')  )
                    else:
                        tmp_result.append( sum(stoneValue[ind: ]) + helper(num_stones, 'L')  )
                return max(tmp_result)
            elif player == 'L':
                tmp_result = []
                for i in range(1, 4):
                    if ind + i <= num_stones:
                        tmp_result.append(helper(ind+i, 'A')  )
                    else:
                        tmp_result.append(helper(num_stones, 'A')  )
                    
                return min(tmp_result)
        
        alex_score = helper(0, 'A')
        
        if alex_score > total_value / 2.:
            return 'Alice'
        elif alex_score < total_value / 2.:
            return 'Bob'
        else:
            return 'Tie'
