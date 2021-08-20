class Solution:

    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        startIndex = 0
        endIndex = len(tokens) - 1
        points = 0
        tokens.sort()
        while True:
            print(startIndex, endIndex, P)
            if startIndex > endIndex or endIndex < startIndex:
                return points
            if P >= tokens[startIndex]:
                points += 1
                P -= tokens[startIndex]
                startIndex += 1
            elif points == 0:
                return points
            elif startIndex == endIndex:
                return points
            else:
                P += tokens[endIndex]
                endIndex -= 1
                points -= 1
