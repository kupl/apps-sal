class Solution:

    def maxWidthRamp(self, A: List[int]) -> int:
        ans = 0
        l = [(n, i) for (i, n) in enumerate(A)]
        l.sort()
        mini = float('inf')
        for e in l:
            mini = min(mini, e[1])
            ans = max(ans, e[1] - mini)
        return ans
