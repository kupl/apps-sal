def power_value(x):
    pv = 0
    while x != 1:
        if x % 2 == 0:
            x = x // 2
        else:
            x = 3 * x + 1
        pv += 1
    return pv

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        power_values = []
        for x in range(lo, hi+1):
            pv_x = power_value(x)
            power_values.append((x,pv_x))
        return sorted(power_values, key=lambda e: e[1])[k-1][0]
                
            
            

