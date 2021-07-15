class Solution:
    def numTeams(self, rating: List[int]) -> int:
        ans = 0
        for i in range(len(rating)):
            a = rating[i]
            for j in range(i+1, len(rating)):
                b = rating[j]
                for k in range(j+1, len(rating)):
                    c = rating[k]
                    if a < b < c or a > b > c:
                        ans += 1
        return ans
