class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        gains = [x if grumpy[i] == 1 else 0 for (i, x) in enumerate(customers)]
        fact = [x if grumpy[i] == 0 else 0 for (i, x) in enumerate(customers)]
        
        if X > len(gains):
            return sum(customers)
        
        current_sum = sum(gains[:X])
        max_gain = current_sum
        for i in range(1, len(gains) - X + 1):
            current_sum = current_sum - gains[i - 1] + gains[i + X - 1]
            max_gain = max(max_gain, current_sum)
        
        return sum(fact) + max_gain

