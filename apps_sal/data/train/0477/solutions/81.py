class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = [0]
        for _ in range(n-1):
            s += [1] + [x ^ 1 for x in reversed(s)]
        return str(s[k-1])
