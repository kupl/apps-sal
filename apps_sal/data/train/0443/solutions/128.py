class Solution:

    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        out = 0
        for i in range(1, n - 1):
            lless = lgreat = rless = rgreat = 0
            for j in range(i - 1, -1, -1):
                if rating[j] > rating[i]:
                    lgreat += 1
                if rating[j] < rating[i]:
                    lless += 1
            for j in range(i + 1, n):
                if rating[j] > rating[i]:
                    rgreat += 1
                if rating[j] < rating[i]:
                    rless += 1
            out += lless * rgreat + lgreat * rless
        return out
