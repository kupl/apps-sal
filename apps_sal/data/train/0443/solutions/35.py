class Solution:
    def numTeams(self, rating: List[int]) -> int:
        count = 0
        for i, r_i in enumerate(rating):
            for j, r_j in enumerate(rating[i+1:], i+1):
                if r_i == r_j:
                    continue

                if r_i < r_j:
                    for k, r_k in enumerate(rating[j+1:], j+1):
                        count += r_j < r_k
                else:
                    for k, r_k in enumerate(rating[j+1:], j+1):
                        count += r_j > r_k
        return count

