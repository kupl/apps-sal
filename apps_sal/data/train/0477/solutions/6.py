class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        full = [0]

        for _ in range(n - 1):
            full = full + [1] + [(x + 1) % 2 for x in full][::-1]

        return str(full[k - 1])
