class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        # use 100, P = 100, p = 1
        # 400 down, P = 500, p = 0
        # use 200, P = 300, p = 1
        # use 300, P = 0, p = 2

        '''
        sort tokens
        play smallest tokens until you can't anymore
        turn over largest tokens until you can play smaller tokens again
        '''
        
        tokens.sort()
        maxPoints = 0
        points = 0
        left, right = 0, len(tokens) - 1
        while left <= right and P >= 0:
            if P - tokens[left] >= 0:
                P -= tokens[left]
                points += 1
                maxPoints = max(maxPoints, points)
                left += 1
            else:
                if points > 0:
                    P += tokens[right]
                    
                    points -= 1
                    right -= 1
                else:
                    break
        
        return max(maxPoints, points)
