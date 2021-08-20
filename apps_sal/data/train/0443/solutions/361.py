class Solution:

    def numTeams(self, rating: List[int]) -> int:
        result = 0
        n = len(rating)
        for i in range(n):
            for j in range(i + 1, n):
                if rating[j] > rating[i]:
                    for k in range(j + 1, n):
                        if rating[k] > rating[j]:
                            result += 1
        for i in range(n):
            for j in range(i + 1, n):
                if rating[j] < rating[i]:
                    for k in range(j + 1, n):
                        if rating[k] < rating[j]:
                            result += 1
        return result
