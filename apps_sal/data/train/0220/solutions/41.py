class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        satisfiedCount = 0

        for i in range(len(customers)):
            if grumpy[i] == 0:
                satisfiedCount += customers[i]
                customers[i] = 0

        maxPotentialCount = 0
        val = 0

        for i in range(len(customers)):
            if i < X:
                val += customers[i]
                continue

            maxPotentialCount = max(maxPotentialCount, val)
            val -= customers[i - X]
            val += customers[i]

        maxPotentialCount = max(maxPotentialCount, val)

        return satisfiedCount + maxPotentialCount
