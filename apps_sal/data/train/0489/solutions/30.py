class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        ind = [i for i in range(len(A))]
        A, ind = zip(*sorted(zip(A, ind)))
        m = len(A)-1
        ans = 0
        for i in range(len(A)):
            ans = max(ind[i] - m, ans)
            m = min(ind[i], m)
        return ans
