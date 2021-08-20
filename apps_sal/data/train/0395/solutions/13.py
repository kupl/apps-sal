class Solution:

    def oddEvenJumps(self, A: List[int]) -> int:
        (n, seen) = (len(A), {})
        (next_higher, next_lower) = ([0] * n, [0] * n)
        stack = []
        for (a, i) in sorted(([a, i] for (i, a) in enumerate(A))):
            while stack and stack[-1] < i:
                next_higher[stack.pop()] = i
            stack.append(i)
        stack = []
        for (a, i) in sorted(([-a, i] for (i, a) in enumerate(A))):
            while stack and stack[-1] < i:
                next_lower[stack.pop()] = i
            stack.append(i)

        def is_possible(ind, jump):
            if ind == n - 1:
                return True
            if (ind, jump) in seen:
                return seen[ind, jump]
            temp = False
            if jump % 2 == 0:
                if next_lower[ind]:
                    temp = is_possible(next_lower[ind], jump + 1)
            elif next_higher[ind]:
                temp = is_possible(next_higher[ind], jump + 1)
            seen[ind, jump] = temp
            return temp
        return sum((1 for i in range(n - 1, -1, -1) if is_possible(i, 1)))
