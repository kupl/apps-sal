class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        satisfied = 0
        for i in range(len(customers)):
            satisfied += customers[i] * (grumpy[i] == 0)

        p = X
        best_imp = sum([customers[i] for i in range(p) if grumpy[i] == 1])
        imp = best_imp
        while p < len(grumpy):
            if grumpy[p] == 1:
                imp += customers[p]
            if grumpy[p - X] == 1:
                imp -= customers[p - X]
            if imp > best_imp:
                best_imp = imp

            p += 1

        return satisfied + best_imp
