class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        index = 0
        n = len(A)
        next_high = [0] * n
        next_low = [0] * n
        stack = []
        B = [[i, a] for i, a in enumerate(A)]
        B.sort(key=lambda x: x[1])
        for i, a in B:
            while stack and (stack[-1] < i):
                next_high[stack.pop()] = i
            stack.append(i)
        B.sort(key=lambda x: -x[1])
        stack = []
        for i, a in B:
            while stack and (stack[-1] < i):
                next_low[stack.pop()] = i
            stack.append(i)

        higher = [0] * n
        lower = [0] * n
        higher[-1] = lower[-1] = 1
        for i in range(n - 2, -1, -1):
            higher[i] = lower[next_high[i]]
            lower[i] = higher[next_low[i]]
        # print(higher, lower)
        return sum(higher)
