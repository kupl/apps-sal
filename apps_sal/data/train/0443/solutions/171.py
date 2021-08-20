class Solution:

    def numTeams(self, rating: List[int]) -> int:
        i = 0
        j = 1
        k = 2
        count = 0
        while i < len(rating) - 2:
            while j < len(rating) - 1:
                while k < len(rating):
                    if rating[i] < rating[j] < rating[k] or rating[i] > rating[j] > rating[k]:
                        count += 1
                    k += 1
                j += 1
                k = j + 1
            i += 1
            j = i + 1
            k = i + 2
        return count
