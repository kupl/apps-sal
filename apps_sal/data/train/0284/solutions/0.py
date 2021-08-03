class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens = sorted(tokens)
        left = 0
        right = len(tokens) - 1
        points = 0

        if len(tokens) == 1:
            if tokens[0] <= P:
                return 1
        if len(tokens) == 0:
            return 0
        while left < right:

            if tokens[left] <= P:
                P -= tokens[left]
                left += 1
                points += 1

            elif tokens[left] > P and points > 0:
                P += tokens[right]
                points -= 1
                right -= 1

            elif points == 0 and tokens[left] > P:
                break
        if P >= tokens[left]:
            points += 1
        return points
