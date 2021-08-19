class Solution:

    def minKBitFlips(self, A: 'List[int]', K: 'int') -> 'int':
        flip = 0
        const = 10
        res = 0
        for i in range(len(A)):
            if flip % 2 != 0:
                if A[i] % 10:
                    res += 1
                    flip += 1
                    if i + K - 1 >= len(A):
                        return -1
                    A[i + K - 1] += const
            elif not A[i] % 10:
                res += 1
                flip += 1
                if i + K - 1 >= len(A):
                    return -1
                A[i + K - 1] += const
            if A[i] > 1:
                flip -= 1
        return res
