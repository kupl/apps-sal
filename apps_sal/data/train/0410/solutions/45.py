class Solution:

    def power_value(self, n):
        count = 0
        while n != 1:
            count += 1
            if n % 2 == 0:
                n /= 2
            else:
                n = n*3 + 1
        return count
    
    def getKth(self, lo: int, hi: int, k: int) -> int:
        vals = sorted(list(range(lo, hi+1)), key=self.power_value)
        return vals[k-1]


