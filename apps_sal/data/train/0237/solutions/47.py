class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        def helper(k):
            if k < 0:
                return 0
            num = 0
            i = 0
            for j in range(len(A)):
                k -= A[j]

                while k < 0:
                    k += A[i]
                    i += 1
                num += j - i + 1
            return num
        return helper(S) - helper(S - 1)
