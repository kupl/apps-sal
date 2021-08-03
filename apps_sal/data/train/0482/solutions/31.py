
class Solution:
    def __init__(self):
        self.vals = None

    def mctFromLeafValues(self, arr):
        self.vals = [[0] * len(arr) for i in range(len(arr))]
        for n in range(2, len(arr) + 1):
            for a in range(len(arr) - n + 1):
                b = a + n
                self.vals[a][b - 1] = min((self.vals[a][i - 1] + self.vals[i][b - 1] + (max(arr[a:i]) * max(arr[i:b]))) for i in range(a + 1, b))
        return self.vals[0][len(arr) - 1]
