class Solution:
    def maxEqualFreq(self, A: List[int]) -> int:

        # Life is hard especially when you think it's easy.
        # Oh my god!!! Please read the problem again. It needs an array prefix of nums!!! Therefore it should start from the first. Shit!!

        counter = collections.Counter()
        fre = [0] * (len(A) + 1)
        res = 0
        for n, a in enumerate(A, 1):
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


#         count = collections.Counter()
#         freq = [0 for _ in range(len(A) + 1)]
#         res = 0
#         for n, a in enumerate(A, 1):

#             # the frequence update, since some number appear again, its appearance affect its count and the frequence.

#             freq[count[a]] -= 1
#             freq[count[a] + 1] += 1
#             c = count[a] = count[a] + 1
#             if freq[c] * c == n and n < len(A):
#                 res = n + 1
#             d = n - freq[c] * c
#             if d in [c + 1, 1] and freq[d] == 1:
#                 res = n
#         return res
