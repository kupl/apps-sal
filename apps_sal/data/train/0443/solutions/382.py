class Solution:
    def numTeams(self, rating: list) -> int:
        left_less, left_greater = 0, 0
        right_less, right_greater = 0, 0
        count = 0
        for j in range(len(rating)):
            for i in range(j):
                if rating[i] < rating[j]:
                    left_less += 1
                elif rating[i] > rating[j]:
                    left_greater += 1
            for k in range(j+1, len(rating)):
                if rating[j] < rating[k]:
                    right_greater += 1
                elif rating[j] > rating[k]:
                    right_less += 1
            count += left_less * right_greater + left_greater * right_less
            left_less = left_greater = right_less = right_greater = 0
        return count
