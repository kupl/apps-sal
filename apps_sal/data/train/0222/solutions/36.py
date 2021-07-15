class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        Aset = set(A)
        res = 0
        for i in range(len(A)-1):
            for j in range(i+1, len(A)):
                a, b = A[i], A[j]
                temp = 2
                while a+b in Aset:
                    temp += 1
                    a, b = b, a+b
                if temp >= 3:
                    res = max(res, temp)
        return res
