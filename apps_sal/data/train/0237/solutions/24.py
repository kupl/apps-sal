class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        if len(A) == 0:
            return 0

        def atmost(m):
            if m < 0:
                return 0

            res = i = 0
            for j in range(len(A)):
                m -= A[j]
                while(m < 0):
                    m += A[i]
                    i += 1
                res += (j - i + 1)
            return res

        return atmost(S) - atmost(S - 1)
