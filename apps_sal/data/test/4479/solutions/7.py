class Solution:

    def largestSumAfterKNegations(self, A: List[int], k: int) -> int:
        d = collections.defaultdict(int)
        for x in A:
            d[x] += 1
        res = 0
        for i in range(-100, 0):
            if i in d and k > 0:
                x = min(k, d[i])
                k -= x
                d[i] -= x
                d[-i] += x
        res = 0
        if k % 2 == 1:
            j = 0
            while j not in d or d[j] <= 0:
                j += 1
            print(j)
            d[j] -= 1
            d[-j] += 1
        for i in range(-100, 101):
            res += d[i] * i
        return res
