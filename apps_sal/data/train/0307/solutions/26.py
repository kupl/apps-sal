class Solution:
    def soupServings(self, N: int) -> float:
        if N > 5555:
            return 1

        memo = dict()

        def Pa(A, B):
            if (A, B) in memo:
                return memo[(A, B)]
            if A <= 0 and B <= 0:
                return 0.5
            if A <= 0:
                return 1
            if B <= 0:
                return 0
            else:
                memo[(A, B)] = (Pa(A - 100, B) + Pa(A - 75, B - 25) + Pa(A - 50, B - 50) + Pa(A - 25, B - 75)) / 4
                return memo[(A, B)]

        return Pa(N, N)
