class Solution:

    def numTeams(self, rating: List[int]) -> int:
        res = 0

        @lru_cache(maxsize=None)
        def check(a, b):
            if rating[a] > rating[b]:
                return 1
            elif rating[a] < rating[b]:
                return 2
            else:
                return 0
        for ind, val in enumerate(rating[2:]):
            ind += 2
            for a in range(ind - 1):
                for b in range(a + 1, ind):
                    c = check(a, b)
                    if c == 1 and val < rating[b] or c == 2 and val > rating[b]:
                        res += 1
        return res
