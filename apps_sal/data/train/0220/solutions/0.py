class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        # feel like its sliding window max
        
        window, max_window = 0, 0
        
        # init first window
        for i in range(X):
            if grumpy[i]: window += customers[i]
        max_window = window
        
        # Sliding Window
        for i in range(X,len(grumpy)):
            if grumpy[i-X]: window -= customers[i-X]
            if grumpy[i]: window += customers[i]
                
            if window > max_window: max_window = window
        
        # 
        sum = 0
        for i in range(len(grumpy)):
            if grumpy[i] == 0: sum += customers[i]
        return sum + max_window
