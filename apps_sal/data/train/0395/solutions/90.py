class Solution:
    def oddEvenJumps(self, A):
        n = len(A)
        next_higher, next_lower = [0] * n, [0] * n

        stack = []
        for a, i in sorted([[a, i] for i, a in enumerate(A)]):
            while stack and stack[-1] < i:
                next_higher[stack.pop()] = i
            stack.append(i)

        stack = []
        for a, i in sorted([[-a, i] for i, a in enumerate(A)]):
            while stack and stack[-1] < i:
                next_lower[stack.pop()] = i
            stack.append(i)

        def jump(index, jump_num):
            if index == n - 1:
                return 1
            next_index = 0
            if jump_num % 2 == 1:
                next_index = next_higher[index]
            else:
                next_index = next_lower[index]
            return jump(next_index, jump_num + 1) if next_index else 0

        result = 0
        for start in range(n):
            result += jump(start, 1)
        return result
