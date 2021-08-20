class Solution:

    def numTeams(self, rating: List[int]) -> int:
        (n, cnt) = (len(rating), 0)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    cnt += rating[i] > rating[j] > rating[k] or rating[i] < rating[j] < rating[k]
        return cnt
