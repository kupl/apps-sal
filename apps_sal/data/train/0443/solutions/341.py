class Solution:

    def numTeams(self, rating: List[int]) -> int:
        count = 0
        for (i, r_i) in enumerate(rating):
            for (j, r_j) in enumerate(rating[i + 1:], i + 1):
                if r_i == r_j:
                    continue
                if r_i < r_j:
                    count += sum((r_j < r_k for r_k in rating[j + 1:]))
                else:
                    count += sum((r_j > r_k for r_k in rating[j + 1:]))
        return count
