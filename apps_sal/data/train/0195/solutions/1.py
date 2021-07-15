class Solution:
    def countTriplets(self, A: List[int]) -> int:
        d = defaultdict(int)
        for a in A:
            for b in A:
                d[a & b] += 1
        return sum(d[ab] for c in A for ab in d if not(ab & c))
