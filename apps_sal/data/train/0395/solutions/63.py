class Solution:

    def oddEvenJumps(self, A: List[int]) -> int:
        l = len(A)
        idxs = sorted(range(l), key=lambda i: A[i])
        odds = [-1] * l
        stack = []
        for i in idxs:
            while stack and stack[-1] < i:
                odds[stack.pop()] = i
            stack.append(i)
        idxs = sorted(range(l), key=lambda i: -A[i])
        evens = [-1] * l
        stack = []
        for i in idxs:
            while stack and stack[-1] < i:
                evens[stack.pop()] = i
            stack.append(i)
        reachable = [[-1, -1] for _ in range(l)]
        reachable[-1] = [1, 1]

        def helper(i, j):
            if reachable[i][j] >= 0:
                return reachable[i][j]
            if j == 0:
                reachable[i][j] = 0 if odds[i] == -1 else helper(odds[i], 1)
            else:
                reachable[i][j] = 0 if evens[i] == -1 else helper(evens[i], 0)
            return reachable[i][j]
        return sum((helper(i, 0) for i in range(l)))
