class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        mymap = {}
        for x in sorted(A):
            # 1 for leaf, plus sum any that could be factors (y and currval/y)
            mymap[x] = 1+ sum(mymap[y]*mymap.get(x/y,0) for y in A if y<x)
        return sum(mymap.values())%(10**9+7)
