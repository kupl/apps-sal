class Solution:
    def numTeams(self, rating: List[int]) -> int:

        i = 0
        final = []
        add = 0
        while i < len(rating):

            j = len(rating) - 1
            while j > i + 1:
                k = j - 1
                while k > i:
                    if rating[i] < rating[k] and rating[k] < rating[j]:
                        add += 1
                    if rating[i] > rating[k] and rating[k] > rating[j]:
                        add += 1
                    k -= 1

                j -= 1
            i += 1
        return add
