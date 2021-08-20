class Solution:

    def reorderedPowerOf2(self, N: int) -> bool:
        sn = sorted(str(N))
        for i in range(32):
            pot = 1 << i
            spot = sorted(str(pot))
            if sn == spot:
                return True
        return False
