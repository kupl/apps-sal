class Solution:

    def findKthBit(self, n: int, k: int) -> str:

        def inner(n, k):
            if n == 1:
                re = 0
            elif k == 2 ** (n - 1):
                re = 1
            elif k < 2 ** (n - 1):
                re = inner(n - 1, k)
            else:
                re = inner(n - 1, 2 ** n - k) ^ 1
            return re
        return str(inner(n, k))
