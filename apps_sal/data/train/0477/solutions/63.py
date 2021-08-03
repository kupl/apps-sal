class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        l = [0]
        for _ in range(n - 1):
            l = l + [1] + [1 - b for b in reversed(l)]
            if len(l) >= k:
                return str(l[k - 1])
        return str(l[k - 1])
