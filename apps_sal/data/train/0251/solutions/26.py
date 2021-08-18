class Solution:
    def clumsy(self, N: int) -> int:

        magic = [1, 2, 2, -1, 0, 0, 3, 3]
        return N + (magic[N % 4] if N > 4 else magic[N + 3])
