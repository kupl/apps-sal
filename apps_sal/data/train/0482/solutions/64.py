class Solution:

    def __init__(self):
        self.dict = {}

    def mctFromLeafValues(self, arr: List[int]) -> int:
        return self.mctHelp(arr, 0, len(arr))

    def mctHelp(self, arr, a, b):
        if b - a == 1:
            self.dict[a, b] = 0
        if (a, b) not in self.dict:
            low = 2 ** 31
            for i in range(a + 1, b):
                res = max(arr[a:i]) * max(arr[i:b]) + self.mctHelp(arr, a, i) + self.mctHelp(arr, i, b)
                low = min(low, res)
            self.dict[a, b] = low
        return self.dict[a, b]
