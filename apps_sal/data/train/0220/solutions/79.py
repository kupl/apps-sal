import itertools as it


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        self.customers = customers
        self.grumpy = grumpy
        self.n = len(customers)
        self.cumulative_customers = list(it.accumulate(customers, initial=0))
        self.technique_length = X
        return self.satisfy(0, 1)

    @lru_cache(None)
    def satisfy(self, index: int, secret_technique: int) -> int:
        if index >= self.n:
            return 0
        satisfaction = self.customers[index] if self.grumpy[index] == 0 else 0
        if secret_technique == 0:
            return satisfaction + self.satisfy(index + 1, 0)
        ans = max(
            satisfaction +
            self.satisfy(index + 1, secret_technique),
            self.cumulative_customers[min(self.n, index + self.technique_length)] -
            self.cumulative_customers[index] +
            self.satisfy(index + self.technique_length, secret_technique - 1),
        )
        return ans
