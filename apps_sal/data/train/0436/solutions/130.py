class Solution:
    def minDays(self, n: int) -> int:
        def number_of_steps(i):
            Q = deque()
            seen_before = set()
            steps = 0
            Q.append((i, steps))
            while True:
                j, steps = Q.popleft()
                if j == 1:
                    return steps
                if j % 3 == 0:
                    branch(Q, seen_before, steps, j - (2 * j // 3))
                if j % 2 == 0:
                    branch(Q, seen_before, steps, j // 2)
                branch(Q, seen_before, steps,  j - 1)

        def branch(Q, seen_before, steps, k):
            if k not in seen_before:
                seen_before.add(k)
                Q.append((k, steps + 1))
        return number_of_steps(n) + 1
