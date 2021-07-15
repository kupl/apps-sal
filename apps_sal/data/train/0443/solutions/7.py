class Solution:
    def numTeams(self, rating: List[int]) -> int:
        return len([1 for i,j,k in itertools.combinations_with_replacement(rating,3) if i<j<k or i>j>k])
