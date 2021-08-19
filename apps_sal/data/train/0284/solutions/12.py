class Solution:
    # all the tokens start in a neutral position. Can either play it face up or face down.
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens.sort()

        # start from front and back. greedily take all the powers from the front and spend score in back to get more to add to the front
        def twoPointer(tokens, P):
            i = 0
            j = len(tokens) - 1
            score = 0
            maxScore = 0
            while i <= j:

                flag = False
                while i < len(tokens) and P >= tokens[i]:
                    score += 1
                    P -= tokens[i]
                    i += 1
                    flag = True
                if flag:
                    maxScore = max(score, maxScore)
                    continue

                if score > 0:
                    score -= 1
                    P += tokens[j]
                    j -= 1

                elif P < tokens[i]:
                    return score
            return maxScore

        def helper(tokens, P, score):
            maxVal = score
            if score > 0 and len(tokens) > 0:
                maxVal = max(helper(tokens[:len(tokens) - 1], P + tokens[len(tokens) - 1], score - 1), maxVal)

            for i in range(len(tokens) - 1, -1, -1):
                if P >= tokens[i]:
                    maxVal = max(helper(tokens[:i] + tokens[i + 1:], P - tokens[i], score + 1), maxVal)
            return maxVal

        return twoPointer(tokens, P)
