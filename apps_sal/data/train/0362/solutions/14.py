from functools import lru_cache


class Solution:

    def numberWays(self, ppl_to_hats: List[List[int]]) -> int:
        hats_to_ppl = [[] for _ in range(41)]
        for (pid, hats) in enumerate(ppl_to_hats):
            for hid in hats:
                hats_to_ppl[hid].append(pid)
        num_ppl = len(ppl_to_hats)
        all_ppl_mask = (1 << num_ppl) - 1
        MOD = 10 ** 9 + 7

        @lru_cache(None)
        def helper(ppl_assigned_bitmask, next_hid):
            if ppl_assigned_bitmask == all_ppl_mask:
                return 1
            if next_hid > 40:
                return 0
            ways = helper(ppl_assigned_bitmask, next_hid + 1) % MOD
            for pid in hats_to_ppl[next_hid]:
                pid_mask = 1 << pid
                if pid_mask & ppl_assigned_bitmask == 0:
                    ways += helper(pid_mask | ppl_assigned_bitmask, next_hid + 1)
                    ways %= MOD
            return ways
        ret = helper(0, 1)
        return ret % MOD
