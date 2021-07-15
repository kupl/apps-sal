class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        if len(arr) <= 1: return 0
        min_i = 0
        min_val = arr[0] * arr[1]
        
        for i in range(1, len(arr) - 1):
            cur = arr[i] * arr[i + 1]
            if cur < min_val:
                min_val = cur
                min_i = i
        
        new_arr = arr[:min_i] + [max(arr[min_i], arr[min_i+1])] + arr[min_i+2:]
        return min_val + self.mctFromLeafValues(new_arr)
