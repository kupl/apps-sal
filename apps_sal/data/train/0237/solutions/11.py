class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        i, s, res, count = 0, 0, 0, 1

        for j in range(len(A)):
            s += A[j]

            while s > S:
                s -= A[i]
                i += 1
                count = 1
            while i < j and A[i] == 0:
                i += 1
                count += 1

            if s == S and i <= j:
                res += count

        return res
