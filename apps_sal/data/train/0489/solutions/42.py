class Solution:

    def maxWidthRamp(self, A: List[int]) -> int:
        mx = 0
        ind = float('inf')
        index = collections.defaultdict(list)
        for (i, x) in enumerate(A):
            index[x].append(i)
        print(index)
        for num in sorted(A):
            mx = max(mx, index[num][-1] - ind)
            ind = min(ind, index[num][0])
        return mx
