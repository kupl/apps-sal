class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        stack = []
        bound = [[0, 0] for x in range(0, len(A))]
        for i in range(0, len(A)):
            if 0 < len(stack):
                if A[i] <= stack[-1][0]:
                    while 0 < len(stack) and A[i] <= stack[-1][0]:
                        bound[stack[-1][1]][1] = i
                        stack.pop()
            stack.append((A[i], i))
        while 0 < len(stack):
            bound[stack[-1][1]][1] = len(A)
            stack.pop()
        index = len(A) - 1
        while 0 <= index:
            if 0 < len(stack):
                if A[index] < stack[-1][0]:
                    while 0 < len(stack) and A[index] < stack[-1][0]:
                        bound[stack[-1][1]][0] = index
                        stack.pop()
            stack.append((A[index], index))
            index -= 1
        while 0 < len(stack):
            bound[stack[-1][1]][0] = -1
            stack.pop()
        sum = 0
        for i in range(0, len(bound)):
            sum += A[i] * (i - bound[i][0]) * (bound[i][1] - i)
            sum %= (10**9 + 7)
        return sum
