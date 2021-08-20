class Solution:

    def numTeams(self, rating: List[int]) -> int:
        ans = []
        n = len(rating)
        for i in range(n):
            for j in range(i, n):
                for k in range(j, n):
                    if rating[i] < rating[j]:
                        if rating[j] < rating[k]:
                            ans.append([rating[i], rating[j], rating[k]])
                    if rating[i] > rating[j]:
                        if rating[j] > rating[k]:
                            ans.append([rating[i], rating[j], rating[k]])
        return len(ans)
