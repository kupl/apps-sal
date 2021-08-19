class Solution:
    def numTeams(self, rating: List[int]) -> int:
        return self.numTeams_brute_force(rating)

    # O(n^3) time and O(1) space solution
    def numTeams_brute_force(self, rating):
        n = 0
        for i in range(len(rating)):
            for j in range(i + 1, len(rating)):
                if rating[j] < rating[i]:
                    for k in range(j + 1, len(rating)):
                        if rating[k] < rating[j]:
                            n += 1
                else:
                    for k in range(j + 1, len(rating)):
                        if rating[k] > rating[j]:
                            n += 1
        return n
