class Solution:

    def sumSubarrayMins(self, A: List[int]) -> int:
        mod = 10 ** 9 + 7
        A = [0] + A + [0]
        q = [-1]
        res = 0
        cur = 0
        for (i, x) in enumerate(A):
            while q and A[q[-1]] > x:
                cur -= A[q[-1]] * (q[-1] - q[-2])
                q.pop()
            res += x * (i - q[-1]) + cur
            cur += x * (i - q[-1])
            q.append(i)
        return res % mod
