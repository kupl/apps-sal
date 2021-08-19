class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:

        m = n = 10**6

        max_area = len(blocked)**2 / 2
        blocked = set(tuple(x) for x in blocked)

        def dfs(r, c, dst, visited, count, steps):
            # print(r, c)
            if (r, c) in visited:
                return False
            if (r, c) == dst:
                return True

            visited.add((r, c))
            if (r, c) in blocked:
                count[0] += 1
                return False

            if 0 <= r < m and 0 <= c < n:
                if count[0] >= 200:
                    return True
                if steps[0] >= max_area:
                    return True

                steps[0] += 1

                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if dfs(r + dr, c + dc, dst, visited, count, steps):
                        return True

            return False

        return dfs(source[0], source[1], tuple(target), set(), [0], [0]) and dfs(target[0], target[1], tuple(source), set(), [0], [0])
