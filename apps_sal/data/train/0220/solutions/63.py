class Solution:

    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        n = len(customers)
        sum_cus = sum(customers)
        for i in range(n):
            customers[i] *= grumpy[i]
        window = 0
        max_secret_satisfied = -math.inf
        (left, right) = (0, 0)
        while right < n:
            window += customers[right]
            right += 1
            while right - left >= X:
                max_secret_satisfied = max(max_secret_satisfied, window)
                window -= customers[left]
                left += 1
        return sum_cus - (sum(customers) - max_secret_satisfied)
