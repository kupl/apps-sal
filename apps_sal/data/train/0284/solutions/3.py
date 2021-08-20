class Solution:

    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens.sort()
        if not tokens or P < tokens[0]:
            return 0
        (l, r) = (0, len(tokens) - 1)
        points = 0
        while l <= r:
            if P >= tokens[l]:
                points += 1
                P -= tokens[l]
                l += 1
            elif r - l > 1:
                points -= 1
                P += tokens[r]
                r -= 1
            else:
                break
        return points
