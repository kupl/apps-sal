class Solution:

    def numOfSubarrays(self, A: List[int]) -> int:
        n = len(A)
        mod = 10 ** 9 + 7
        ans = 0
        (p, ctr) = ([0] * (n + 1), Counter([0]))
        for i in range(n):
            p[i] = p[i - 1] + A[i]
            s = p[i] % 2
            ans = ans + ctr[1 - s]
            ans = ans % mod
            ctr[s] += 1
        return ans
