class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        def get_power_of_element(x):
            if x == 1:
                return 0
            elif x % 2 == 0:
                x = x/2
                return 1+get_power_of_element(x)
            elif x % 2 != 0:
                x = 3*x + 1
                return 1+get_power_of_element(x)
        
        array_of_numbers = [x for x in range(lo, hi+1)]
        hash_map = {}
        for i in array_of_numbers:
            k_value = get_power_of_element(i)
            hash_map[i] = k_value

        array_of_values = [(y, x) for x, y in list(hash_map.items())]
        array_of_values.sort(key=lambda x: x[0])
        
        return array_of_values[k-1][1]
        

