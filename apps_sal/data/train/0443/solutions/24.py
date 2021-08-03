class Solution:
    def numTeams(self, rating: List[int]) -> int:
        count = 0
        for i, r_i in enumerate(rating):
            for j, r_j in enumerate(rating[i + 1:], i + 1):
                for k, r_k in enumerate(rating[j + 1:], j + 1):
                    count += r_i < r_j < r_k or r_i > r_j > r_k
        return count
