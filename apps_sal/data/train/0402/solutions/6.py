class Solution:

    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:

        def method1(blocked):
            R = C = 10 ** 6
            if not (0 <= source[0] < R and 0 <= source[1] < C):
                return False
            if not (0 <= target[0] < R and 0 <= target[1] < C):
                return False
            if not blocked:
                return True
            blocked = set(map(tuple, blocked))
            seen = set()

            def neighbors(r, c):
                for (nr, nc) in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                    if 0 <= nr < R and 0 <= nc < C:
                        yield (nr, nc)

            def dfs(r, c):
                if (r, c) in seen:
                    return False
                if [r, c] == target:
                    return True
                if (r, c) in blocked:
                    return False
                seen.add((r, c))
                for (nr, nc) in neighbors(r, c):
                    if dfs(nr, nc):
                        return True
                return False
            return dfs(*source)

        def method2(blocked):
            if not blocked:
                return True
            blocked = set(map(tuple, blocked))

            def neighbors(r, c):
                for (nr, nc) in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                    if 0 <= nr < R and 0 <= nc < C:
                        yield (nr, nc)

            def check(blocked, source, target):
                (si, sj) = source
                (ti, tj) = target
                level = 0
                q = collections.deque([(si, sj)])
                vis = set()
                while q:
                    for _ in range(len(q)):
                        (i, j) = q.popleft()
                        if i == ti and j == tj:
                            return True
                        for (x, y) in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                            if 0 <= x < 10 ** 6 and 0 <= y < 10 ** 6 and ((x, y) not in vis) and ((x, y) not in blocked):
                                vis.add((x, y))
                                q.append((x, y))
                    level += 1
                    if level == len(blocked):
                        return True
                return False
            return check(blocked, source, target) and check(blocked, target, source)
        return method2(blocked)
