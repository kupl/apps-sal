class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        S = set(A)

        ans = 2
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                a = A[i]
                b = A[j]
                l = 2
                while((a + b) in S):
                    temp = a
                    a = b
                    b = temp + b
                    l += 1

                ans = max(ans, l)

        if ans < 3:
            return 0
        return ans
