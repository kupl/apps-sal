class Solution:

    def numSubarraysWithSum(self, A: List[int], S: int) -> int:

        def atMostK(A, S):
            if S < 0:
                return 0
            i = res = 0
            for j in range(len(A)):
                S -= A[j]
                while S < 0:
                    S += A[i]
                    i += 1
                res += j - i + 1
            return res
        return atMostK(A, S) - atMostK(A, S - 1)
