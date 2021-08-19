class Solution:

    def numTeams(self, rating: List[int]) -> int:
        ans = 0
        for (i, j, k) in combinations(rating, 3):
            if i < j < k or i > j > k:
                ans += 1
        return ans
