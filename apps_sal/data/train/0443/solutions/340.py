class Solution:
    def numTeams(self, rating: List[int]) -> int:
        cnt = 0
        for i in range(len(rating) - 2):
            for j in range(i + 1, len(rating) - 1):
                if rating[j] > rating[i]:
                    cnt += len([k for k in rating[j+1:len(rating)] if k > rating[j]])
                if rating[j] < rating[i]:
                    cnt += len([k for k in rating[j+1:len(rating)] if k < rating[j]])
        return cnt
