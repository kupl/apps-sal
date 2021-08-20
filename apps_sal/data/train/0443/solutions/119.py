class Solution:

    def numTeams(self, rating: List[int]) -> int:
        count = 0
        for idx0 in range(len(rating) - 2):
            for idx1 in range(idx0 + 1, len(rating) - 1):
                for idx2 in range(idx1 + 1, len(rating)):
                    if rating[idx0] < rating[idx1] and rating[idx1] < rating[idx2]:
                        count += 1
                    elif rating[idx0] > rating[idx1] and rating[idx1] > rating[idx2]:
                        count += 1
        return count
