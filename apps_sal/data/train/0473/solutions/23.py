class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        d = defaultdict(set)
        s = 0
        d[0].add(-1)
        for i,x in enumerate(arr):
            s ^= x
            d[s].add(i)

        return sum([abs(a-b)-1 for k in d for a,b in combinations(d[k],2)])   

