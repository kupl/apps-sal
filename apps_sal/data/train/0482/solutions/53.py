class Solution:

    def __init__(self):
        self.vals = None

    def mctFromLeafValues(self, arr: List[int]) -> int:
        self.vals = [[0] * len(arr) for i in range(len(arr))]
        return self.mctHelp(arr, 0, len(arr))

    def mctHelp(self, arr, a, b):
        if b - a == 1:
            return 0
        if self.vals[a][b - 1] == 0:
            low = 2 ** 30
            for i in range(a + 1, b):
                res = self.mctHelp(arr, a, i) + self.mctHelp(arr, i, b) + max(arr[a:i]) * max(arr[i:b])
                if res < low:
                    low = res
            self.vals[a][b - 1] = low
        return self.vals[a][b - 1]
