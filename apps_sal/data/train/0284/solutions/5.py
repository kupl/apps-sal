class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
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
