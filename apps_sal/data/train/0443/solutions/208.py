class Solution:
    def numTeams(self, rating: List[int]) -> int:
        answer = 0
        n = len(rating)

        for i in range(n):
            for j in range(n):
                if j < i:
                    continue
                for k in range(n):
                    if j < k:
                        if rating[i] < rating[j] < rating[k]:
                            answer += 1
                        elif rating[i] > rating[j] > rating[k]:
                            answer += 1

        return answer
