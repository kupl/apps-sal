class Solution:
    def numTeams(self, rating: List[int]) -> int:
        count = len(rating)
        if count < 3:
            return 0
        result = 0
        for i in range(count-2):
            for j in range(i+1, count-1):
                increasing = rating[j] > rating[i]
                for k in range(j+1, count):
                    if increasing and rating[k] > rating[j]:
                        result += 1
                    elif not increasing and rating[k] < rating[j]:
                        result += 1
        return result
