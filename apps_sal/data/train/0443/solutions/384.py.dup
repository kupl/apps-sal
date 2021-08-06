class Solution:
    def numTeams(self, rating: List[int]) -> int:
        import itertools
        return len([1 for i, j, k in itertools.combinations(rating, 3) if i < j < k or i > j > k])
