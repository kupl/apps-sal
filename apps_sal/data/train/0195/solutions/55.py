class Solution:
    def countTriplets(self, A: List[int]) -> int:
        c = Counter(x & y for x in A for y in A)
        return sum(c[xy] for xy in c for z in A if xy & z == 0)
