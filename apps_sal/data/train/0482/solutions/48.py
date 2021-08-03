class Solution:
    def ans(self, start, end, arr, dp):
        product = 999999999999999
        maxleaf = -1
        if start == end:
            return arr[start], 0
        for i in range(start, end):
            if (start, end) in dp:
                return dp[(start, end)]
            a, b = self.ans(start, i, arr, dp)
            c, d = self.ans(i + 1, end, arr, dp)
            maxleaf = max(a, c)
            product = min(product, a * c + b + d)
        dp[(start, end)] = (maxleaf, product)
        return maxleaf, product

    def mctFromLeafValues(self, arr: List[int]) -> int:
        dp = {}
        return self.ans(0, len(arr) - 1, arr, dp)[1]
