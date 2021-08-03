class Solution:
    def numTeams(self, rating: List[int]) -> int:
        # find all ascending and descending combos in order of length three
        # o(n^3) solution
        count = 0
        i = 0
        while i < len(rating):
            j = i + 1
            while j < len(rating):
                k = j + 1
                while k < len(rating):
                    if (rating[i] > rating[j] > rating[k]) or (rating[i] < rating[j] < rating[k]):
                        count += 1
                    k += 1
                j += 1
            i += 1
        return count
