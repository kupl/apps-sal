class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        power_dic = {}
        powers = []
        for num in range(lo, hi+1):
            powers.append([self.powerOf(num, 0, power_dic), num])
        return sorted(powers, key=lambda x:x[0])[k-1][1]
            
    
    
    def powerOf(self, x, steps, power_dic):
        if x==1:
            return steps
        if x&1 == 0:
            return self.powerOf(x//2, steps+1, power_dic)
        else:
            return self.powerOf(3*x+1, steps+1, power_dic)

