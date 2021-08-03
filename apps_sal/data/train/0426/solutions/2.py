class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:

        # Because 10**9 ~ 2**30
        return sorted(str(N)) in [sorted(str(1 << i)) for i in range(30)]
