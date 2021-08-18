
class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        hat2ppl = defaultdict(set)
        for p, hats_i in enumerate(hats):
            for h in hats_i:
                hat2ppl[h].add(p)
        if len(hats) > len(hat2ppl):
            return 0
        M = 10**9 + 7

        @lru_cache(None)
        def dfs(h, mask):
            if h == 42:
                return 0
            if bin(mask).count('1') == len(hats):
                return 1
            ans = dfs(h + 1, mask)
            for p in hat2ppl[h]:
                x = 1 << p
                if mask & x == 0:
                    mask |= x
                    ans += dfs(h + 1, mask)
                    mask ^= x
            return ans % M
        return dfs(1, 0) % M
