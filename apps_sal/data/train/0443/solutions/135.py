class Solution:
    def numTeams(self, rating: List[int]) -> int:
        if len(rating) < 3:
            return 0

        teamsCount = 0

        for i in range(len(rating) - 2):
            for j in range(i + 1, len(rating) - 1):
                for k in range(j + 1, len(rating)):
                    if (
                        (rating[i] > rating[j] > rating[k])
                        or (rating[i] < rating[j] < rating[k])
                    ):
                        teamsCount += 1

        return teamsCount
