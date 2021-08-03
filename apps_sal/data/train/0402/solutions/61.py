class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        blocked = set(map(tuple, blocked))
        src, target = tuple(source), tuple(target)

        # src和target要分别作为起点试一下，防止target被包围了但是source还是可以走很远的情况
        # dfs里的seen要单独输入set(), 否则会沿用上一次dfs的seen而影响结果
        return self.dfs(src, target, set(), blocked) and self.dfs(target, src, set(), blocked)

    def dfs(self, src, target, seen, blocked):

        if len(seen) > 20000 or src == target:
            return True

        x0, y0 = src
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            x = x0 + dx
            y = y0 + dy
            if (0 <= x < 10**6 and 0 <= y < 10**6 and ((x, y) not in seen) and ((x, y) not in blocked)):
                seen.add((x, y))
                if self.dfs((x, y), target, seen, blocked):
                    return True

        return False
