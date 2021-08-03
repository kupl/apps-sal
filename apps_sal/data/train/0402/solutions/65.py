from collections import deque


class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        if not blocked:
            return True
        blocked = set(map(tuple, blocked))

        def check(source, target):
            si, sj = source
            ti, tj = target
            level = 0
            q = deque([(si, sj)])
            seen = set()
            while q:
                for _ in range(len(q)):
                    i, j = q.popleft()
                    if i == ti and j == tj:
                        return True
                    for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                        if 0 <= x < 10**6 and 0 <= y < 10**6 and (x, y) not in seen and (x, y) not in blocked:
                            seen.add((x, y))
                            q.append((x, y))
                level += 1
                if level == len(blocked):
                    break
            else:
                return False
            return True

        return check(source, target) and check(target, source)
