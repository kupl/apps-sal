class Solution:

    def numTeams(self, rating: List[int]) -> int:
        result = 0
        for i in range(len(rating)):
            for j in range(i + 1, len(rating)):
                if rating[j] == rating[i]:
                    continue
                if rating[j] < rating[i]:
                    result += sum((num < rating[j] for num in rating[j + 1:]))
                else:
                    result += sum((num > rating[j] for num in rating[j + 1:]))
        return result
