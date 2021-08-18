class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        currentTurb = [1, 1]
        maxTurb = max(currentTurb)
        ALength = len(A)
        for i in range(1, ALength):
            currentNum = A[i]
            previousNum = A[i - 1]
            a, b = currentTurb
            if currentNum > previousNum:
                currentTurb = [1, a + 1]
            elif currentNum < previousNum:
                currentTurb = [b + 1, 1]
            else:
                currentTurb = [1, 1]
            maxTurb = max(max(currentTurb), maxTurb)
        return maxTurb
