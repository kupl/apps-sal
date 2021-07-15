class Solution:
    def countTriplets(self, A: List[int]) -> int:
        combo = collections.Counter(x&y for x in A for y in A)
        return sum(combo[k] for z in A for k in combo if z&k == 0)
