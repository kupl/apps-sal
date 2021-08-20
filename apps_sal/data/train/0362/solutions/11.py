class Solution:

    def numberWays(self, hats: List[List[int]]) -> int:
        hat_to_ppl = [[] for _ in range(41)]
        for (i, person) in enumerate(hats):
            for hat_preference in person:
                hat_to_ppl[hat_preference].append(i)
        hat_to_ppl = list([x for x in hat_to_ppl if x])
        num_hats = len(hat_to_ppl)
        num_ppl = len(hats)
        if num_hats < num_ppl:
            return 0

        @functools.lru_cache(None)
        def dp(i, mask):
            if i == num_hats:
                if bin(mask).count('1') == num_ppl:
                    return 1
                else:
                    return 0
            res = dp(i + 1, mask)
            for person in hat_to_ppl[i]:
                if mask & 1 << person == 0:
                    mask |= 1 << person
                    res += dp(i + 1, mask)
                    mask ^= 1 << person
            return res % (10 ** 9 + 7)
        return dp(0, 0)
