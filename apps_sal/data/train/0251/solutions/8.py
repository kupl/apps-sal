class Solution:

    def clumsy(self, N: int) -> int:
        stack = []
        j = -1
        for i in range(N, 0, -1):
            stack.append(i)
            if j % 4 == 0 or (j % 4 == 1 and len(stack) > 1):
                x = stack.pop()
                y = stack.pop()
                if j % 4 == 0:
                    stack.append(x * y)
                elif j % 4 == 1:
                    stack.append(y // x)
            j += 1
        res = stack[0]
        for j in range(1, len(stack), 2):
            res += stack[j]
            if j != len(stack) - 1:
                res -= stack[j + 1]
        return res
