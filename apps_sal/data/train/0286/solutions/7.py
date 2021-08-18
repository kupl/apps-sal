class Solution:
    def getProbability(self, balls: List[int]) -> float:
        N = len(balls)
        sm = sum(balls)
        half = sm // 2

        @lru_cache(None)
        def rec2(cur, na, nb):
            if na > half or nb > half:
                return 0
            if cur == N:
                return int(na == nb)

            ans = 0
            for i in range(balls[cur] + 1):
                remplacea, remplaceb = (half - na), (half - nb)
                choice = math.comb(remplacea, i) * math.comb(remplaceb, balls[cur] - i)
                ans += rec2(cur + 1, na + i, nb + balls[cur] - i) * choice

            return ans

        @lru_cache(None)
        def rec(cur, na, nb, uniquea, uniqueb):
            if na > half or nb > half:
                return 0
            if cur == N:
                if na != nb or uniquea != uniqueb:
                    return 0
                return 1

            gg = 0
            for i in range(balls[cur] + 1):
                toa, tob = na + i, nb + balls[cur] - i
                ua, ub = uniquea + int(i > 0), uniqueb + int(balls[cur] - i > 0)

                remplacea, remplaceb = (half - na), (half - nb)
                choice = math.comb(remplacea, i) * math.comb(remplaceb, balls[cur] - i)
                gg += rec(cur + 1, toa, tob, ua, ub) * choice

            return gg

        gg = rec(0, 0, 0, 0, 0)
        permutation = math.factorial(sm) / math.factorial(half)
        al = rec2(0, 0, 0)
        return gg / al
