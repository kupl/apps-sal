class Solution:
    def numOfSubarrays(self, A: List[int]) -> int:
        n = len(A)
        mod = 10**9 + 7
        ans = 0
        prefix, ctr = 0, Counter([0])
        for i in range(n):
            prefix = prefix + A[i]
            s = prefix % 2
            ans = ans + ctr[1 - s]
            ans = ans % mod
            ctr[s] += 1
        return ans
