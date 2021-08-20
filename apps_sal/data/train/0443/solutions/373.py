class Solution:

    def numTeams(self, rating: List[int]) -> int:
        cnt = 0
        for i in range(1, len(rating) - 1):
            s_l = 0
            s_r = 0
            l_l = 0
            l_r = 0
            for j in range(0, i):
                if rating[j] < rating[i]:
                    s_l += 1
                elif rating[j] > rating[i]:
                    l_l += 1
            for k in range(i + 1, len(rating)):
                if rating[k] > rating[i]:
                    s_r += 1
                elif rating[k] < rating[i]:
                    l_r += 1
            cnt += s_l * s_r + l_l * l_r
        return cnt
