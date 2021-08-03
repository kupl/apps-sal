class Solution:
    def numTeams(self, rating: List[int]) -> int:
        size = len(rating)
        count = 0
        for i in range(size):
            for j in range(i + 1, size):
                for k in range(j + 1, size):
                    if rating[i] < rating[j] < rating[k] or rating[i] > rating[j] > rating[k]:
                        count += 1
        return count
