class Solution:
    def numTeams(self, rating: List[int]) -> int:
        # brute force
        length = len(rating)
        ans = []

        for i in range(length - 2):
            temp = rating[i]

            for j in range(i + 1, length):
                if rating[j] > temp:
                    for k in range(j + 1, length):
                        if rating[k] > rating[j]:
                            ans.append([rating[i], rating[j], rating[k]])

                if rating[j] < temp:
                    for k in range(j + 1, length):
                        if rating[k] < rating[j]:
                            ans.append([rating[i], rating[j], rating[k]])

        return len(ans)
