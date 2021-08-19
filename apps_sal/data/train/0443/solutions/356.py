class Solution:
    def numTeams(self, rating: List[int]) -> int:
        # brute force
        length = len(rating)
        ans = 0

        for i in range(length - 2):
            temp = rating[i]

            for j in range(i + 1, length):
                if rating[j] > temp:
                    for k in range(j + 1, length):
                        if rating[k] > rating[j]:
                            ans += 1

                if rating[j] < temp:
                    for k in range(j + 1, length):
                        if rating[k] < rating[j]:
                            ans += 1

        return ans
