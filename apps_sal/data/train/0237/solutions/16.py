class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        return self.at_most(A, S) - self.at_most(A, S - 1)

    def at_most(self, A, S):
        if S < 0:
            return 0

        start = 0
        res = 0
        for end in range(len(A)):
            S -= A[end]
            while start < len(A) and S < 0:
                S += A[start]
                start += 1

            res += (end - start + 1)
        return res
