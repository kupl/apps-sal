class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        i = 0
        for j in range(1, n + 1):
            if n%j == 0:
                i += 1
            if i == k:
                return j
        return -1

