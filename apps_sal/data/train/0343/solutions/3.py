class Solution:
    def numSquares(self, n):
        """
        四平方和定理
        :type n: int
        :rtype: int
        """
        while n % 4 == 0:
            n //= 4
        if n % 8 == 7:
            return 4
        for i in range(n + 1):
            tmp = i * i
            if tmp <= n:
                if int((n - tmp) ** 0.5) ** 2 + tmp == n:
                    return 1 + (0 if tmp == 0 else 1)
            else:
                break
        return 3
