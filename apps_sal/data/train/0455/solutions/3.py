class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        a = [(math.inf, math.inf, -math.inf, -math.inf) for _ in range(61)]
        source = [[0] * len(targetGrid[0]) for _ in targetGrid]
        for i in range(len(targetGrid)):
            for j in range(len(targetGrid[i])):
                a[targetGrid[i][j]] = (min(a[targetGrid[i][j]][0], j), min(a[targetGrid[i][j]][1], i), max(a[targetGrid[i][j]][2], j), max(a[targetGrid[i][j]][3], i))
        gr = defaultdict(set)
        for p in range(len(a)):
            x, y, z, t = a[p]
            if x != math.inf:
                for i in range(y, t + 1):
                    for j in range(x, z + 1):
                        if targetGrid[i][j] != p:
                            gr[p].add(targetGrid[i][j])
        visited = set()
        inp = set()
        def dfs(k):
            inp.add(k)
            for x in gr[k]:
                if x in inp:
                    return False
                elif x not in visited and not dfs(x):
                    return False
            inp.remove(k)
            visited.add(k)
            return True
        for i in range(61):
            if i not in visited and not dfs(i):
                return False
        return True

