class Solution:
    def maxWidthRamp(self, a: List[int]) -> int:
        sis = sorted(list(range(len(a))), key=a.__getitem__)
        return max(i - m for m, i in zip(itertools.accumulate(sis, min), sis))
