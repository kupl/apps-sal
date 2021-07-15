class Solution:
    def numTeams(self, rating: List[int]) -> int:
        y, x, ans = 0, 0, 0
        for i in rating[:-2]:
            for j in rating[x+1:-1]:
                for k in rating[y+2:]:
                    if i < j < k or i > j > k:                  
                        ans += 1
                y += 1
            x += 1
            y = x
        return ans
