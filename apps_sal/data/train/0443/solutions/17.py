class Solution:
    def numTeams(self, rating: List[int]) -> int:
        ret, n = 0, len(rating)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                if rating[j] > rating[i]:
                    for k in range(j + 1, n):
                        if rating[k] > rating[j]:
                            ret += 1
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                if rating[j] < rating[i]:
                    for k in range(j + 1, n):
                        if rating[k] < rating[j]:
                            ret += 1
        return ret
