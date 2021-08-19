class Solution:

    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:

        def bfs(source, target):
            (r0, c0) = source
            (rd, cd) = target
            seen = {(r0, c0)}
            dq = deque([(r0, c0)])
            N = 10 ** 6
            cnt = 0
            while dq:
                (r, c) = dq.popleft()
                cnt += 1
                if r == rd and c == cd or cnt > 19900:
                    return True
                for (ro, co) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    (nr, nc) = (r + ro, c + co)
                    if 0 <= nr < N and 0 <= nc < N and ((nr, nc) not in seen) and ((nr, nc) not in bset):
                        seen.add((nr, nc))
                        dq.append((nr, nc))
            return False
        bset = {tuple(b) for b in blocked}
        return bfs(source, target) and bfs(target, source)
