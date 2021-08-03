class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        s = []
        for i in hours:
            if i > 8:
                s.append(1)
            else:
                s.append(-1)

        n = len(s)
        presum = [0] * (n + 1)
        for i in range(1, (n + 1)):
            presum[i] = presum[i - 1] + s[i - 1]

        stack = []
        n = len(presum)
        for i in range(n):
            if not stack or presum[stack[-1]] > presum[i]:
                stack.append(i)
        res = 0
        i = n - 1
        while i > res:
            while stack and presum[stack[-1]] < presum[i]:
                res = max(res, i - stack[-1])
                stack.pop()
            i -= 1
        return res
