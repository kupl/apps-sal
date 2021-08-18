class Solution:

    def soupServings(self, N: int) -> float:

        if N >= 12500:
            return 1

        self.memory = {}
        return self.helper(N, N)

    def helper(self, A, B):

        if (A, B) in self.memory:
            return self.memory[(A, B)]
        elif A <= 0 and B <= 0:
            return 0.5
        elif B <= 0:
            return 0
        elif A <= 0:
            return 1

        prob = 0
        prob += 0.25 * self.helper(A - 100, B)

        prob += 0.25 * self.helper(A - 75, B - 25)

        prob += 0.25 * self.helper(A - 50, B - 50)

        prob += 0.25 * self.helper(A - 25, B - 75)

        self.memory[(A, B)] = prob
        return prob
