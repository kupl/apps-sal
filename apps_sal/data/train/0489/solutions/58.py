class Solution:

    def maxWidthRamp(self, A: List[int]) -> int:
        mx = 0
        ind = float('inf')
        index = collections.defaultdict(list)
        for (i, x) in enumerate(A):
            index[x].append(i)
        for i in sorted(A):
            mx = max(mx, index[i][-1] - ind)
            ind = min(ind, index[i][0])
        return mx
