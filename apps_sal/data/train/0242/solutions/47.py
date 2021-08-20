class Solution:

    def maxEqualFreq(self, A: List[int]) -> int:
        counter = collections.Counter()
        fre = [0] * (len(A) + 1)
        res = 0
        for (n, a) in enumerate(A, 1):
            c = counter[a]
            fre[c] -= 1
            fre[c + 1] += 1
            c += 1
            counter[a] += 1
            if c * fre[c] == n and n < len(A):
                res = n + 1
            d = n - c * fre[c]
            if d in [1, c + 1] and fre[d] == 1:
                res = n
        return res
