class Solution:
    def numTeams(self, rating: List[int]) -> int:
        i = 0
        j = i + 1
        k = j + 1
        result = 0
        while (i < len(rating) - 2):
            if k == len(rating):
                j += 1
                k = j

            if (j == len(rating)):
                i += 1
                j = i + 1
                k = j

            if rating[i] < rating[j] and rating[j] < rating[k]:
                result += 1
            elif rating[i] > rating[j] and rating[j] > rating[k]:
                result += 1

            k += 1
        return result
