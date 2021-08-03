class Solution:
    def getProbability(self, balls: List[int]) -> float:
        @lru_cache(None)
        def select(n, r):
            if r > n:
                return 0
            if r == 0:
                return 1
            if r == 1:
                return n
            return select(n - 1, r) + select(n - 1, r - 1)

        @lru_cache(None)
        def dputil(i, j, pos, n):
            if pos == -1:
                if n == 0:
                    return 1
                else:
                    return 0
            p2 = 1 << pos
            if i & p2 and j & p2:
                ans = 0
                for x in range(1, balls[pos]):
                    diff = n - 2 * x + balls[pos]
                    ans += dputil(i, j, pos - 1, diff) * select(balls[pos], x)
                return ans
            if i & p2:
                return dputil(i, j, pos - 1, n - balls[pos])
            else:
                return dputil(i, j, pos - 1, n + balls[pos])

        def numsplits(n):
            cnt = 0
            while n:
                cnt += n % 2
                n = n // 2
            return cnt

        k = len(balls)
        tot = sum(balls)
        k2 = 1 << k
        valid = 0
        for i in range(k2):
            for j in range(k2):
                if (i | j != k2 - 1) or numsplits(i) != numsplits(j):
                    continue
                valid += dputil(i, j, k - 1, 0)
        return float(valid) / float(select(tot, tot // 2))
