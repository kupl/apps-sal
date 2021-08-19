class Solution:

    def minOperations(self, n: int) -> int:
        A = [_ * 2 + 1 for _ in range(n)]
        ret = 0
        for i in range(0, n // 2):
            ret += n - i * 2 - 1
        return ret
