class Solution:

    def numTeams(self, rating: List[int]) -> int:
        count = 0
        for (i, s1) in enumerate(rating[:-2]):
            for (j, s2) in enumerate(rating[i + 1:-1]):
                if s2 > s1:
                    for s3 in rating[i + j + 2:]:
                        if s3 > s2:
                            count += 1
                else:
                    for s3 in rating[i + j + 2:]:
                        if s3 < s2:
                            count += 1
        return count
