class Solution:
    def numTeams(self, rating: List[int]) -> int:
        N = len(rating)
        numteams = 0

        for i in range(N):
            left = 0
            right = 0

            for j in range(N):
                if(j < i):
                    if(rating[j] < rating[i]):
                        left += 1
                elif(j > i):
                    if(rating[i] < rating[j]):
                        right += 1
            numteams += (left * right)

        for i in range(N):
            left = 0
            right = 0

            for j in range(N):
                if(j < i):
                    if(rating[i] < rating[j]):
                        left += 1
                elif(j > i):
                    if(rating[i] > rating[j]):
                        right += 1
            numteams += (left * right)

        return numteams
