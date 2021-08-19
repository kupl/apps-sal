class Solution:

    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        n = len(A)

        def num_subar_at_most(lim):
            subarr_ct = 0
            r_sum = 0
            li = 0
            for ri in range(n):
                r_sum += A[ri]
                while li <= ri and r_sum > lim:
                    r_sum -= A[li]
                    li += 1
                subarr_ct += ri - li + 1
            return subarr_ct
        return num_subar_at_most(S) - num_subar_at_most(S - 1)
