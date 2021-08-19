class Solution:

    def numTeams(self, rating: List[int]) -> int:
        l = len(rating)
        res = 0
        for (i, r1) in enumerate(rating[:l - 2]):
            for j in range(i + 1, l - 1):
                r2 = rating[j]
                if r1 > r2:
                    for k in range(j + 1, l):
                        r3 = rating[k]
                        if r2 > r3:
                            res += 1
                if r1 < r2:
                    for k in range(j + 1, l):
                        r3 = rating[k]
                        if r2 < r3:
                            res += 1
        return res
