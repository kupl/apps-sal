class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if d == 0:
            return 0
        q = collections.deque([(i + 1, 1) for i in range(f)])
        visited = {(0, 0): 1}
        while q:
            (s, di) = q.popleft()
            if (s, di) in visited:
                continue
            npath = sum((visited.get((s - i - 1, di - 1), 0) for i in range(f)))
            if di == d:
                if s == target:
                    return npath % 1000000007
                else:
                    continue
            visited[s, di] = npath
            q += [(s + i + 1, di + 1) for i in range(f)]
        return 0
