class Solution:
    # 2D dp, where count[i][f] indicates the number of ways after i throw and at face f and total[i] indicates the total number of ways after i throw.
    # count[0][f] = 0 and total[0] = 1.
    # for each throw, check the number of ways to after ith throw and the end face is f
    # def dieSimulator(self, n: int, rollMax: List[int]) -> int:

    # DFS with memoization.
    # State to remember (#throws_left, #repeat, last_face)
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        cache = collections.defaultdict()

        def dfs(n, repeat, face):
            if n == 0:
                return 1
            elif (n, repeat, face) in cache:
                return cache[(n, repeat, face)]
            else:
                count = 0
                for f in range(6):
                    if f != face:
                        count += dfs(n - 1, 1, f)
                    else:
                        if repeat + 1 <= rollMax[f]:
                            count += dfs(n - 1, repeat + 1, f)
                cache[(n, repeat, face)] = count
                return count

        return sum(dfs(n - 1, 1, f) for f in range(6)) % (10**9 + 7)
