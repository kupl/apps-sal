class Solution:
    ans = 0

    def bfs(self, index, even, odd, curr):
        if index == len(even) - 1:
            self.ans += 1
            return
        if curr % 2 == 0:
            if even[index] != -1:
                self.bfs(even[index], even, odd, curr + 1)
        else:
            if odd[index] != -1:
                self.bfs(odd[index], even, odd, curr + 1)

    def oddEvenJumps(self, A: List[int]) -> int:
        self.ans = 0
        s = sorted(list(range(len(A))), key=lambda i: A[i])
        a = [-1] * len(A)
        b = [-1] * len(A)
        stack = []
        for val in s:
            while len(stack) > 0 and stack[-1] < val:
                a[stack.pop()] = val
            stack.append(val)
        s = sorted(list(range(len(A))), key=lambda i: A[i], reverse=True)
        stack = []
        for val in s:
            while len(stack) > 0 and stack[-1] < val:
                b[stack.pop()] = val
            stack.append(val)

        for i, val in enumerate(s):
            self.bfs(i, b, a, 1)
        return self.ans
