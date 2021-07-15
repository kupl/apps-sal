class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        def bfs(source, target):
            seen = set()
            queue = collections.deque([source])
            while queue:
                if len(seen) >= 19901: return True
                for _ in range(len(queue)):
                    pos = queue.popleft()
                    if pos == target: return True
                    seen.add(pos)
                    i, j = pos
                    for ni, nj in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                        if 0 <= ni < 10**6 and 0 <= nj < 10**6 and (ni, nj) not in blocked and (ni, nj) not in seen:
                            if (ni, nj) == target: return True
                            seen.add((ni, nj))
                            queue.append((ni, nj))
            return False

            
        blocked = set(map(tuple, blocked))
        source, target = tuple(source), tuple(target)
        return bfs(source, target) and bfs(target, source)
            

