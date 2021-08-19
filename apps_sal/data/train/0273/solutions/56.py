class Solution:

    def racecar(self, target: int) -> int:
        bq = collections.deque([(0, 1, 0)])
        visited = set((0, 1))
        while bq:
            (p, s, step) = bq.popleft()
            if p == target:
                return step
            if (p + s, 2 * s) not in visited:
                bq.append((p + s, 2 * s, step + 1))
                visited.add((p + s, 2 * s))
            ns = 1 if s < 0 else -1
            if (p, ns) not in visited:
                bq.append((p, ns, step + 1))
                visited.add((p, ns))
