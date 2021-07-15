class Solution:
    power = {}
    def get_power(self, num):
        if num == 1:
            return 0
        if num in self.power:
            return self.power[num]
        if num % 2 == 0:
            self.power[num] = self.get_power(num // 2) + 1
        else:
            self.power[num] = self.get_power(3 * num + 1) + 1
        
        return self.power[num]
    
    def getKth(self, lo: int, hi: int, k: int) -> int:
        power_vals = {
            val: self.get_power(val) for val in range(lo, hi+1)
        }
        vals = [k for k, v in sorted(power_vals.items(), key=lambda x: (x[1], x[0]))]
        return vals[k-1]
