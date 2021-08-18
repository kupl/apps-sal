class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        maxlen = 10**6
        maxarea = 40000
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        blocked = set(map(tuple, blocked))

        def bfs(source, target):
            q = collections.deque()
            aset = set()
            q.append(source)
            while q and len(aset) < maxarea:
                row, col = q.popleft()
                if row == target[0] and col == target[1]:
                    return True
                aset.add((row, col))

                for dir in dirs:
                    row2 = row + dir[0]
                    col2 = col + dir[1]
                    if 0 <= row2 < maxlen and 0 <= col2 < maxlen and not (row2, col2) in aset and not (row2, col2) in blocked:
                        q.append([row2, col2])
                        aset.add((row2, col2))
            return len(aset) >= maxarea
        return bfs(source, target) and bfs(target, source)
