class Solution:

    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        satisfied = []
        satisfied_before = 0
        satisfied_after = sum([x[0] for x in zip(customers[X:], grumpy[X:]) if not x[1]])
        for i in range(len(customers) - X + 1):
            satisfied.append(satisfied_before + sum(customers[i:i + X]) + satisfied_after)
            if not grumpy[i]:
                satisfied_before += customers[i]
            if i + X < len(customers) and (not grumpy[i + X]):
                satisfied_after -= customers[i + X]
        return max(satisfied)
