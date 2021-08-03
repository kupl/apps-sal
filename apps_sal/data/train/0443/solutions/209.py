class Solution:

    def numTeams(self, rating: List[int]) -> int:
        arr = []
        for i in range(len(rating) - 2):
            for j in range(i + 1, len(rating) - 1):
                for k in range(j + 1, len(rating)):
                    if (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]):
                        arr.append([rating[i], rating[j], rating[k]])
        if arr:
            return len(arr)
        return 0
