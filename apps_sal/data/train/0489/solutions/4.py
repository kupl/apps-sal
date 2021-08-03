class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        idxs = sorted(range(len(A)), key=lambda i: A[i])

        ramp = 0
        mini = len(A)
        for idx in idxs:
            mini = min(mini, idx)
            ramp = max(ramp, idx - mini)
        return ramp
