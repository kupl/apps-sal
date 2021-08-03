class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        # for each index k, we will find the largest array that is turbulent where we consider cases being ending with a decrease, and ending with an increase.
        currentTurb = [1, 1]  # indicates ending on decrease, ending on increase
        maxTurb = max(currentTurb)
        ALength = len(A)
        for i in range(1, ALength):
            currentNum = A[i]
            previousNum = A[i - 1]  # be careful about what you are calling previous (check indices)
            a, b = currentTurb
            if currentNum > previousNum:
                currentTurb = [1, a + 1]
            elif currentNum < previousNum:  # don't forget to specify elif
                currentTurb = [b + 1, 1]
            else:
                currentTurb = [1, 1]  # since we can't have any turbulence now
            maxTurb = max(max(currentTurb), maxTurb)
        return maxTurb
