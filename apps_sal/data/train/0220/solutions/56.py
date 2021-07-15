class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        N = len(grumpy)
        
        already_happy = sum(customers[i] for i in range(N) if not grumpy[i])
                
        window = sum(customers[i] for i in range(X) if grumpy[i])
        
        max_bonus = window
        for r in range(X, N):
            window -= customers[r - X] if grumpy[r - X] else 0
            window += customers[r] if grumpy[r] else 0
            max_bonus = max(max_bonus, window)
                    
        return already_happy + max_bonus
