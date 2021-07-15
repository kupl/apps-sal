class Solution:
    def getMaxLen(self, a: List[int], having_zero=True) -> int:
        if not a: return 0
        if having_zero: 
            zeros = [i for i, x in enumerate(a) if x == 0]        
            ans, prev = -float('inf'), 0            
            for i in zeros:
                ans = max(ans, self.getMaxLen(a[prev:i], False))
                prev = i+1
            ans = max(ans, self.getMaxLen(a[prev:], False))
            return ans        
        negs = [i for i, x in enumerate(a) if x < 0]
        if len(negs) % 2 == 0: return len(a)
        return max(negs[-1], len(a) - negs[0] - 1)
