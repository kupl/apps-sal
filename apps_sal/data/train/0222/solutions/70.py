class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        s = set(A)
        res = 2
        for i in range(len(A)):
            for j in range(i+1,len(A)):
                a = A[i]
                b = A[j]
                l = 2
                while a + b in s:
                    a,b,l = b,a + b,l + 1
                res = max(res,l) % (10 ** 9 + 7)
        return res if res > 2 else 0
