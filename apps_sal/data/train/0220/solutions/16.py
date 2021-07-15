class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        mp = lp = sum(customers[i] for i in range(X) if grumpy[i])
        mi = 0
        for i in range(1, len(grumpy) - X + 1):
            n = customers[i+X-1] if grumpy[i+X-1] else 0
            o = customers[i-1] if grumpy[i-1] else 0
            lp += (n - o)
            if lp > mp:
                mp = lp
                mi = i
        res = sum([customers[i] for i in range(len(grumpy)) if not grumpy[i]])
        return res + mp
                
                

