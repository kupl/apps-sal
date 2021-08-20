class Solution:

    def numTeams(self, rating: List[int]) -> int:
        count = 0
        length = len(rating)
        if length < 3:
            return 0
        for i in range(length):
            for j in range(i + 1, length):
                for k in range(j + 1, length):
                    if rating[i] > rating[j] > rating[k] or rating[i] < rating[j] < rating[k]:
                        count += 1
        return count
