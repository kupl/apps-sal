class Solution:
    def numTeams(self, rating: List[int]) -> int:
        res = 0
        l = [0] * len(rating)
        m = [0] * len(rating)
        for p, q in enumerate(rating):
            for j in range(p):
                if rating[j] < q:
                    l[p] += 1
                    res += l[j]
                else:
                    m[p] += 1
                    res += m[j]
        return res
