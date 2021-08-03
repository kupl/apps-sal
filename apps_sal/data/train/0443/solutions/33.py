from itertools import combinations


class Solution:

    def numTeams(self, rating: List[int]) -> int:
        cnt = 0
        for i in range(0, len(rating) - 2):
            if rating[i] == rating[i + 1]:
                continue
            for j in range(i + 1, len(rating) - 1):
                for k in range(j + 1, len(rating)):
                    if rating[i] > rating[j]:
                        if rating[j] > rating[k]:
                            cnt += 1
                    elif rating[j] < rating[k]:
                        cnt += 1
        return cnt
