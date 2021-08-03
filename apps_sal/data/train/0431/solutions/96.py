class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        n = len(A)
        left = [0] * n
        right = [0] * n
        s1 = []
        s2 = []
        mod = 10 ** 9 + 7
        for i in range(n):
            cnt = 1
            while s1 and s1[-1][0] > A[i]:
                cnt += s1.pop()[1]
            s1.append((A[i], cnt))
            left[i] = cnt
        for i in range(n - 1, -1, -1):
            cnt = 1
            while s2 and s2[-1][0] >= A[i]:
                cnt += s2.pop()[1]
            s2.append((A[i], cnt))
            right[i] = cnt
        return sum(A[i] * left[i] * right[i] for i in range(n)) % mod
