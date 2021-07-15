class Solution:
    def numTeams(self, rating: List[int]) -> int:
        answer = 0
        is_increasing = False
        for i in range(len(rating)-2):
            for j in range(i+1, len(rating)-1):
                if rating[i] == rating[j]:
                    continue

                is_increasing = rating[i] < rating[j]
                for k in range(j+1, len(rating)):
                    if is_increasing and rating[j] < rating[k]:
                        answer += 1
                    elif not is_increasing and rating[j] > rating[k]:
                        answer += 1

        return answer
