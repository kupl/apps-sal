import collections


class Solution(object):
    def numberWays(self, hats):
        lp = len(hats)
        mod = 10**9 + 7
        h_dict = collections.defaultdict(set)
        for i, h in enumerate(hats):
            for val in h:
                h_dict[val].add(i)
        key_hats = list(h_dict.keys())
        lk = len(key_hats)

        @lru_cache(None)
        def arrange(idx, peo):

            if peo == (1 << lp) - 1:
                return 1
            if idx >= lk:
                return 0
            re = arrange(idx + 1, peo)
            for nt in h_dict[key_hats[idx]]:
                if peo & 1 << nt == 0:
                    re += arrange(idx + 1, peo | 1 << nt)
            return re % mod

        return arrange(0, 0) % mod
