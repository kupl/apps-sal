class Solution(object):
    def sumSubarrayMins(self, A):
        MOD = 10**9 + 7
        N = len(A)

        # prev has i* - 1 in increasing order of A[i* - 1]
        # where i* is the answer to query j
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
        # next has k* + 1 in increasing order of A[k* + 1]
        # where k* is the answer to query j
        stack = []
        nxt = [None] * N
        for k in range(N - 1, -1, -1):
            count = 1
            while stack and A[k] < A[stack[-1][0]]:
                x, c = stack.pop()
                count += c
            stack.append((k, count))
            nxt[k] = stack[-1][1] if stack else N

        # Use prev/next array to count answer
        print(nxt)
        return sum((prev[i]) * (nxt[i]) * A[i]
                   for i in range(N)) % MOD
