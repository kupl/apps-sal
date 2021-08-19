class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        # sliding window of possible grumping times
        satisfied = 0
        n = len(customers)
        grumpySum = [0] * (n - X + 1)

        for i in range(X):
            satisfied += customers[i] if grumpy[i] == 0 else 0

            saved = customers[i] if grumpy[i] == 1 else 0
            grumpySum[0] += saved

        noGrump = grumpySum[0]
        for i in range(X, n):
            satisfied += customers[i] if not grumpy[i] else 0

            saved = customers[i] if grumpy[i] else 0
            abandon = customers[i - X] if grumpy[i - X] else 0
            grumpySum[i - X + 1] = grumpySum[i - X] + saved - abandon
            noGrump = max(noGrump, grumpySum[i - X + 1])

        return satisfied + noGrump
