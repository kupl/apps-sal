class Solution:

    def sumSubseqWidths(self, A: List[int]) -> int:
        A.sort()
        LIM = 10 ** 9 + 7
        res = 0
        powTable = [1]
        for _ in range(len(A)):
            powTable.append(2 * powTable[-1] % LIM)
        for (i, val) in enumerate(A):
            res = (res + val * powTable[i] - val * powTable[len(A) - i - 1]) % LIM
        return res
