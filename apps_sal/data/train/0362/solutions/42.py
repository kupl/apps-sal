class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        N = len(hats)

        @lru_cache(None)
        def helper(mask, i):
            if i == 41:
                if mask == 0:
                    return 1
                else:
                    return 0
            elif mask == 0:
                return 1
            else:
                total = 0
                for pers in range(N):
                    if mask & (1 << pers) and i in hats[pers]:
                        total += helper(mask ^ (1 << pers), i + 1)
                total += helper(mask, i + 1)
                return total

        return helper(2**N - 1, 1) % (10**9 + 7)
