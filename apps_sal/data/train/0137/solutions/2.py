class Solution:

    def minimumOneBitOperations(self, n: int) -> int:
        if n <= 1:
            return n
        b = int(math.log2(n)) + 1
        return (1 << b) - 1 - self.minimumOneBitOperations(n - (1 << b - 1))
