
class Solution:
    def __init__(self):
        self.dict = {}
    def mctFromLeafValues(self, arr: List[int]) -> int:
        return self.mctHelp(arr, 0, len(arr))
        
    def mctHelp(self, arr, a, b):
        if b-a == 1:
            return 0
        if (a,b) not in self.dict:
            low, idx = 2**30, -1
            for i in range(a+1, b):
                res =  self.mctHelp(arr, a, i) + self.mctHelp(arr, i, b)
                if res < low:
                    low = res
                    idx = i
            low += max(arr[a:idx])*max(arr[idx:b])
            self.dict [a,b] = low
        return self.dict [a,b]
