class Solution:

    def maxSatisfied(self, customers: List[int], grumpy: List[int], window_size: int) -> int:

        already_satisfied = 0
        for index in range(len(customers)):
            if grumpy[index] == 0:
                already_satisfied += customers[index]
                customers[index] = 0

        best_satisfied = 0

        satisfied = 0
        for index, customer in enumerate(customers):
            satisfied += customer

            if index >= window_size:
                satisfied -= customers[index - window_size]

            best_satisfied = max(best_satisfied, satisfied)

        return best_satisfied + already_satisfied
