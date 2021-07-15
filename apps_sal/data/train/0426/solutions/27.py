class Solution:
    def reorderedPowerOf2(self, N):
        c = sorted(str(N))
        for i in range(32):
            if sorted(str(1 << i)) == c:
                return True
        return False
