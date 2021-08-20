class Solution:

    def oddEvenJumps(self, A: List[int]) -> int:
        N = len(A)

        def makeStack(S):
            ret = [None] * N
            stack = []
            for i in S:
                while stack and i > stack[-1]:
                    ret[stack.pop()] = i
                stack.append(i)
            return ret
        S = sorted(list(range(N)), key=lambda i: A[i])
        odd = makeStack(S)
        S = sorted(list(range(N)), key=lambda i: A[i], reverse=True)
        even = makeStack(S)
        dp = [[0, 0]] * N
        dp[N - 1] = [1, 1]
        for i in range(N - 2, -1, -1):
            dp[i] = [0, 0]
            if odd[i] is not None:
                dp[i][1] = dp[odd[i]][0]
            if even[i] is not None:
                dp[i][0] = dp[even[i]][1]
        cnt = 0
        for i in range(N):
            cnt += dp[i][1]
        return cnt
