class Solution:
    def oddEvenJumps(self, B: List[int]) -> int:
        A = [[v, i] for i, v in enumerate(B)]
        A.sort()
        nextHigher = [len(A)] * (len(A) + 1)
        nextSmaller = [len(A)] * (len(A) + 1)
        stack = collections.deque()
        for v, i in A:
            while stack and stack[-1] < i:
                nextHigher[stack.pop()] = i
            stack.append(i)

        stack = collections.deque()
        A = [[-v, i] for i, v in enumerate(B)]
        A.sort()
        for v, i in A:
            while stack and stack[-1] < i:
                nextSmaller[stack.pop()] = i
            stack.append(i)

        dp = [[False, False] for _ in range(len(A) + 1)]
        dp[-2] = [True, True]  # even, odd jump
        res = 1
        for i in range(len(A) - 2, -1, -1):
            nH, nL = nextHigher[i], nextSmaller[i]
            dp[i][0] = dp[nL][1]
            dp[i][1] = dp[nH][0]
            res += dp[i][1]
        return res
