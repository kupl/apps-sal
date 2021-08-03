class Solution:

    def lenLongestFibSubseq(self, A: List[int]) -> int:
        s = set(A)
        maxi = 2

        for i in range(len(A) - 2):

            for j in range(i + 1, len(A) - 1):
                c = 2
                a = A[j]
                b = A[i] + A[j]
                while(b in s):
                    c += 1
                    a, b = b, a + b
                maxi = max(maxi, c)

        return maxi if maxi > 2 else 0
