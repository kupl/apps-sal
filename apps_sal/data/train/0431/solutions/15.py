class Solution(object):
    def sumSubarrayMins(self, A):
        MOD = 10**9 + 7
        N = len(A)

        stack = []
        prev = [None] * N
        for i in range(N):
            count = 1
            while stack and A[i] <= A[stack[-1][0]]:
                x, c = stack.pop()
                count += c
            stack.append((i, count))
            prev[i] = stack[-1][1] if stack else -1

        print(prev)
        stack = []
        nxt = [None] * N
        for k in range(N - 1, -1, -1):
            count = 1
            while stack and A[k] < A[stack[-1][0]]:
                x, c = stack.pop()
                count += c
            stack.append((k, count))
            nxt[k] = stack[-1][1] if stack else N

        print(nxt)
        return sum((prev[i]) * (nxt[i]) * A[i]
                   for i in range(N)) % MOD
