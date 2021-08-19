import functools


class Solution:

    def minDays(self, n: int) -> int:
        min_cnt = {}
        visited = set()

        @functools.lru_cache(maxsize=None)
        def dfs(num, cnt):
            visited.add(num)
            if num == 1:
                return cnt + 1
            minres = 2 * 10 ** 9
            if num in min_cnt:
                min_cnt[num] = min(min_cnt[num], cnt)
            else:
                min_cnt[num] = cnt
            if num % 3 == 0:
                minres = min(minres, dfs(num // 3, cnt + 1))
            if num % 2 == 0:
                minres = min(minres, dfs(num // 2, cnt + 1))
            if not (num + 3 in min_cnt and cnt >= min_cnt[num + 3]) or (num - 1 in min_cnt and cnt + 1 < min_cnt[num - 1]):
                minres = min(minres, dfs(num - 1, cnt + 1))
            return minres
        return dfs(n, 0)
