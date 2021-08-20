class Solution:

    def numTeams(self, rating: List[int]) -> int:
        if len(rating) <= 2:
            return 0
        res = 0
        for i in range(len(rating) - 2):
            incs = []
            decs = []
            for j in range(i + 1, len(rating) - 1):
                if rating[j] > rating[i]:
                    incs.append(j)
                elif rating[j] < rating[i]:
                    decs.append(j)
            for ind in incs:
                for j in range(ind + 1, len(rating)):
                    if rating[j] > rating[ind]:
                        res += 1
            for ind in decs:
                for j in range(ind + 1, len(rating)):
                    if rating[j] < rating[ind]:
                        res += 1
        return res
