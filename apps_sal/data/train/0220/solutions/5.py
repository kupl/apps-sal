class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        base = sum(c for c, g in zip(customers, grumpy) if g == 0)
        ncus = [c if g == 1 else 0 for c, g in zip(customers, grumpy)]
        length = len(customers)
        return base + max(sum(ncus[i:i+X]) for i in range(0, length-X+1))
            
            

