class Solution:
    def findKthBit(self, n: int, k: int) -> str:

        d = dict()
        d[0] = [0]
        for i in range(1, n + 1):
            d[i] = d[i - 1] + [1] + [1 - x for x in d[i - 1]][::-1]

        return str(d[n][k - 1])
