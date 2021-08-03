from collections import deque


class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        if not blocked:
            return True
        blocked = set(tuple(b) for b in blocked)

        def util(source, target):
            si, sj = source
            ti, tj = target
            step = 0
            q = deque([(si, sj)])
            seen = {(si, sj)}

            while q:
                step += 1
                if step == len(blocked):
                    return True
                for _ in range(len(q)):
                    i, j = q.popleft()
                    if i == ti and j == tj:
                        return True
                    for r, c in [(i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)]:
                        if 0 <= r < 1000000 and 0 <= c < 1000000 and (r, c) not in blocked and (r, c) not in seen:
                            seen.add((r, c))
                            q.append((r, c))

            return False

        return util(source, target) and util(target, source)
