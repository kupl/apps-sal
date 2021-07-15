class Solution:
    def __init__(self):
        self.memo = {}
    def getKth(self, lo: int, hi: int, k: int) -> int:
        power = [0 for i in range(lo, hi + 1)]
        for i in range(lo, hi + 1):
            if i in self.memo:
                power[i - lo] = self.memo[i]
            else:    
                power[i - lo] = (self.get_power(i, 0), i)
                self.memo[i] = power[i - lo]
        
        power.sort()
        return power[k - 1][1]    
        
    def get_power(self, i, curr_pow):
        if i == 1:
            return curr_pow
        if i % 2 == 0:
            return self.get_power(i / 2, curr_pow + 1)
        else:
            return self.get_power((i - 1) / 2 * 3 + 2, curr_pow + 2)
