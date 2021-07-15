class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        if not blocked:
            return True
        M, N = 10 ** 6, 10 ** 6
        blocked = set(map(tuple, blocked))
        
        def bfs(src, tgt):
            q = collections.deque([tuple(src)])
            k = 0
            seen = set(tuple(src))
            while q:
                i, j = q.popleft()
                k += 1
                if [i, j] == tgt or k == 20000:
                    return True
                for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                    if 0 <= x < M and 0 <= y < N and (x, y) not in seen and (x, y) not in blocked:
                        seen.add((x, y))
                        q.append((x, y))
            return False
        
        return bfs(source, target) and bfs(target, source)
