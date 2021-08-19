class Solution:

    def findKthBit(self, n: int, k: int) -> str:
        series = ['0']
        for i in range(n - 1):
            series = self.getNext(series)
        return series[k - 1]

    def getNext(self, series):
        extension = series[::-1]
        for (idx, c) in enumerate(extension):
            if c == '0':
                extension[idx] = '1'
            else:
                extension[idx] = '0'
        return series + ['1'] + extension
