class Solution:
    def numTeams(self, rating: List[int]) -> int:
        lens = len(rating)
        count = 0
        for i in range(lens - 1):
            for j in range(i + 1, lens - 1):
                for k in range(j + 1, lens):
                    if (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]):
                        count += 1

        return count
