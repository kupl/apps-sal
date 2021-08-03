class Solution:
    def mctFromLeafValues(self, arr):
        vals = [[0] * len(arr) for i in range(len(arr))]
        maxes = [[0] * len(arr) for i in range(len(arr))]
        for n in range(1, len(arr) + 1):
            for a in range(len(arr) - n + 1):
                b = a + n
                maxes[a][b - 1] = max(maxes[a][b - 2], arr[b - 1])
                if n >= 2:
                    vals[a][b - 1] = min((vals[a][i - 1] + vals[i][b - 1] + (maxes[a][i - 1] * maxes[i][b - 1]) for i in range(a + 1, b)))
        print(vals)
        return vals[0][len(arr) - 1]
