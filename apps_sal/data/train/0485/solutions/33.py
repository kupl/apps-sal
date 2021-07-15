class Solution:
    def minKBitFlips(self, A: 'List[int]', K: 'int') -> 'int':
        flip = 0
        const = 10
        res = 0
        for i in range(len(A)):
            temp = A[i] % 10
            if flip % 2 != 0:
                if temp:
                    res += 1
                    flip += 1
                    if i + K - 1 < len(A):
                        A[i + K - 1] += const
                    else:
                        return -1
            else:
                if not temp:
                    res += 1
                    flip += 1
                    if i + K - 1 < len(A):
                        A[i + K - 1] += const
                    else:
                        return -1
            if A[i] > 1:
                flip -= 1
        return res
