class Solution:

    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens.sort()
        max_points = 0
        points = 0
        i = 0
        j = len(tokens) - 1

        while i <= j:
            if P >= tokens[i]:
                points += 1
                P -= tokens[i]
                max_points = max(points, max_points)
                i += 1
            elif points > 0:
                points -= 1
                P += tokens[j]
                j -= 1
            else:
                return max_points

        return max_points
