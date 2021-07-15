class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        n = len(tokens)
        tokens.sort()
        i = 0
        j = n-1
        points = 0
        result = 0
        
        while i <= j:
            if tokens[i] <= P:
                points += 1
                result = max(result, points)
                P -= tokens[i]
                i += 1
            else:
                if points == 0:
                    break
                P += tokens[j]
                points -= 1
                j -= 1
        
        return result
