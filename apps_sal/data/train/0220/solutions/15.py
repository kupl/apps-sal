class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        max_satisfaction = sum(customers)
        actual_satisfaction = sum(int(not g) * s for g,s in zip(grumpy, customers))
        
        max_s_x = sum(customers[:X])
        actual_s_x = sum(int(not g) * s for g,s in zip(grumpy[:X], customers[:X]))
        
        ans = actual_satisfaction - actual_s_x + max_s_x
        for i in range(X, len(customers)):
            max_s_x += customers[i] - customers[i - X]
            actual_s_x += (customers[i] * int(not grumpy[i])) - (customers[i - X] * int(not grumpy[i - X]))
            ans = max(ans, actual_satisfaction - actual_s_x + max_s_x)
        return ans
