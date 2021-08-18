from collections import deque


class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        n = len(A)
        if n == 1:
            return 1
        dp_even, dp_odd = [False] * (n + 1), [False] * (n + 1)

        even_jumps, odd_jumps = [-1] * n, [-1] * n
        asc_sorted = sorted((val, i) for i, val in enumerate(A))
        desc_sorted = sorted((-val, i) for i, val in enumerate(A))
        stack = deque()
        for val, i in asc_sorted:
            while stack and stack[-1] < i:
                odd_jumps[stack.pop()] = i
            stack.append(i)
        stack = deque()
        for val, i in desc_sorted:
            while stack and stack[-1] < i:
                even_jumps[stack.pop()] = i
            stack.append(i)

        dp_even[n - 1] = dp_odd[n - 1] = True
        for i in reversed(range(n - 1)):
            dp_even[i] = dp_odd[even_jumps[i]]
            dp_odd[i] = dp_even[odd_jumps[i]]
        return dp_odd.count(True)
