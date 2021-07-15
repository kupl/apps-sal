class PowerValue(tuple):
    def __lt__(x, y):
        
        return x[1] < y[1] if x[1] != y[1] else x[0] < y[0]
    

        
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        all_val = [i for i in range(lo, hi+1)]
        pow_values = []
        
        def power(val):
            if val == 1:
                return 0

            if val % 2 == 0:
                val = val // 2
            else:
                val = (3 * val + 1)
        
            return 1 + power(val)
        
        for num in all_val:
            get_pow = power(num)
            pow_values.append((get_pow, num))
        pow_values.sort()
        
        return pow_values[k-1][1]
        
        

