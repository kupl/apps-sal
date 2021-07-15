class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        # sliding window of possible grumping times
        satisfied = 0
        n = len(customers)
        grumpySum = 0
        
        for i in range(X):
            satisfied += customers[i] if grumpy[i] == 0 else 0
            
            saved = customers[i] if grumpy[i] == 1 else 0
            grumpySum += saved

        noGrump = grumpySum
        for i in range(X, n):
            satisfied += customers[i] if not grumpy[i] else 0
            
            saved = customers[i] if grumpy[i] else 0
            abandon = customers[i - X] if grumpy[i - X] else 0
            grumpySum = grumpySum + saved - abandon
            noGrump = max(noGrump, grumpySum)

        return satisfied + noGrump
       
          

