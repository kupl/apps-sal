class Solution:
    pow2 = set()
    for i in range(30):
        pow2.add(''.join(sorted(str(1 << i))))

    def reorderedPowerOf2(self, N: int) -> bool:
        return ''.join(sorted(str(N))) in self.pow2
