class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:

        stoneN = len(stoneValue)
        totalScore = sum(stoneValue)

        dp = {}

        def play(i0, ARound):
            if i0 == stoneN:
                return 0
            if (i0, ARound) in dp:
                return dp[(i0, ARound)]
            if ARound:
                subAns = float('-inf')
                thisRoundScore = 0
                for j in range(i0, min(i0 + 3, stoneN)):
                    thisRoundScore += stoneValue[j]
                    subAns = max(subAns, thisRoundScore + play(j + 1, False))
            else:
                subAns = float('inf')
                for j in range(i0, min(i0 + 3, stoneN)):
                    subAns = min(subAns, play(j + 1, True))

            dp[(i0, ARound)] = subAns
            return subAns

        aScore = play(0, True)
        bScore = totalScore - aScore

        if aScore == bScore:
            return 'Tie'
        elif aScore > bScore:
            return 'Alice'
        else:
            return 'Bob'
