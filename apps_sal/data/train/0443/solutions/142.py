class Solution:
    def numTeams(self, rating: List[int]) -> int:
        counts = 0

        for ix in range(len(rating) - 2):
            for iy in range(ix, len(rating) - 1):
                for iz in range(iy, len(rating)):
                    if rating[ix] < rating[iy] and rating[iy] < rating[iz]:
                        counts += 1
                    elif rating[ix] > rating[iy] and rating[iy] > rating[iz]:
                        counts += 1
        return counts
