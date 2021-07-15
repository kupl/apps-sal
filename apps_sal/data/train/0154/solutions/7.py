class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        if 0 not in horizontalCuts:
            horizontalCuts.append(0)
        if h not in horizontalCuts:
            horizontalCuts.append(h)
        if 0 not in verticalCuts:
            verticalCuts.append(0)
        if w not in verticalCuts:
            verticalCuts.append(w)
        horizontalCuts.sort()
        verticalCuts.sort()
        i = 0
        max_diff = -float('inf')
        while i in range(len(horizontalCuts)-1):
            if horizontalCuts[i+1]-horizontalCuts[i] > max_diff:
                max_diff = max(max_diff, horizontalCuts[i+1]-horizontalCuts[i])
            i += 1
        j = 0
        max_diff1 = -float('inf')
        while j in range(len(verticalCuts)-1):
            if verticalCuts[j+1] - verticalCuts[j] > max_diff1:
                max_diff1 = max(max_diff1, verticalCuts[j + 1] - verticalCuts[j])
            j += 1
        return (max_diff*max_diff1)%((10**9)+7)
