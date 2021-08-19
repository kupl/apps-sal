class Solution:

    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        if n < 3:
            return 0
        greater = [0] * n
        smaller = [0] * n
        for i in range(len(rating) - 1):
            for j in range(i + 1, len(rating), 1):
                if rating[j] > rating[i]:
                    greater[j] += 1
                elif rating[j] < rating[i]:
                    smaller[j] += 1
        total = 0
        for j in range(1, len(rating), 1):
            for k in range(j + 1, len(rating), 1):
                if rating[k] > rating[j]:
                    total += greater[j]
                elif rating[k] < rating[j]:
                    total += smaller[j]
        return total
