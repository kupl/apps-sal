class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        stack = []
        ans = accu = 0
        for i, h in enumerate(hours):
            if h > 8:
                accu += 1
            else:
                accu -= 1
            if accu > 0:
                ans = i + 1
            else:
                L, U = -1, len(stack)
                while L + 1 < U:
                    m = (L + U) // 2
                    if stack[m][1] < accu:
                        U = m
                    else:
                        L = m
                if U < len(stack):
                    ans = max(ans, i - stack[U][0])
            if not stack or stack[-1][1] > accu:
                stack.append((i, accu ))
        return ans

