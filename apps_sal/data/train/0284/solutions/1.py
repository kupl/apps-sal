class Solution:
    
    # O(nlog(n) + n) = O(n(log(n) + 1)) = O(nlog(n)) time / O(1) space or memory
    # Where 'n' is the number of tokens passed in the input
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        # we wanna maximize the points in this game (by giving the power to get points)
        # we can give point away to get power
        tokens.sort() # O(mlog(m))
        max_points = 0
        points = 0
        i = 0
        j = len(tokens) - 1
        
        while i <= j:
            if P >= tokens[i]:
                points += 1 # get a coin
                P -= tokens[i] # give up power
                max_points = max(points, max_points)
                i += 1
            elif points > 0:
                points -= 1 # give up that coin
                P += tokens[j] # get power
                j -= 1
            else:
                return max_points
            
        return max_points
