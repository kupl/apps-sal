class Solution:

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        cache = collections.defaultdict()

        def dfs(n, repeat, face):
            if n == 0:
                return 1
            elif (n, repeat, face) in cache:
                return cache[n, repeat, face]
            else:
                count = 0
                for f in range(6):
                    if f != face:
                        count += dfs(n - 1, 1, f)
                    elif repeat + 1 <= rollMax[f]:
                        count += dfs(n - 1, repeat + 1, f)
                cache[n, repeat, face] = count
                return count
        return sum((dfs(n - 1, 1, f) for f in range(6))) % (10 ** 9 + 7)
