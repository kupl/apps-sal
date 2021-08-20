class Solution:

    def numberWays(self, hats: List[List[int]]) -> int:
        N = len(hats)
        ppl = dict()
        for (i, hat) in enumerate(hats):
            for x in hat:
                ppl.setdefault(x, []).append(i)

        @lru_cache(None)
        def helper(h, mask):
            if mask == (1 << N) - 1:
                return 1
            if h == 40:
                return 0
            ans = helper(h + 1, mask)
            for p in ppl.get(h + 1, []):
                if mask & 1 << p:
                    continue
                mask |= 1 << p
                ans += helper(h + 1, mask)
                mask ^= 1 << p
            return ans % 1000000007
        return helper(0, 0)
