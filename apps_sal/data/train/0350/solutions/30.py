class Window:
    def __init__(self):
        self.count = collections.Counter()
        self.nonzero = 0
    def add(self, x):
        self.count[x] += 1
        if self.count[x] == 1:
            self.nonzero += 1
    def remove(self, x):
        self.count[x] -= 1
        if self.count[x] == 0:
            self.nonzero -= 1
            
class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        window1 = Window()
        window2 = Window()
        ans = le1 = le2 = 0
        
        for ri, val in enumerate(A):
            window1.add(val)
            window2.add(val)
            
            while window1.nonzero > K:
                window1.remove(A[le1])
                le1 += 1
            while window2.nonzero >= K:
                window2.remove(A[le2])
                le2 += 1
            
            ans += le2 - le1
        return ans

