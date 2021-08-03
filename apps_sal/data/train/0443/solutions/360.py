class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        res = 0

        for p in range(n - 2):
            for q in range(p + 1, n - 1):
                if rating[p] > rating[q]:
                    for o in range(q + 1, n):
                        if rating[q] > rating[o]:
                            res += 1

        for p in range(n - 2):
            for q in range(p + 1, n - 1):
                if rating[p] < rating[q]:
                    for o in range(q + 1, n):
                        if rating[q] < rating[o]:
                            res += 1
        return res
