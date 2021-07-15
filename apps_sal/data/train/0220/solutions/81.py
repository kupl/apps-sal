class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        
        window = [0] * X
        for a in range(X):
            if grumpy[a] == 1:
                window[a] += customers[a]
        mySum = 0
        maxAdded = sum(window)
        right = X
        for i in range(len(customers)):
            if i + X < len(customers):
                window.pop(0)
                window.append(customers[i+X] if grumpy[i+X] == 1 else 0)
                if sum(window) > maxAdded: maxAdded = sum(window)
            if grumpy[i] == 0: mySum += customers[i] 
        
        return mySum + maxAdded
                    
            

