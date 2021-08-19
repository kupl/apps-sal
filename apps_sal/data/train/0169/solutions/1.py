class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """

        import math
        if n == 2 or n == 3:
            return n - 1
        else:
            if n % 3 == 1:
                m1 = 2
            elif n % 3 == 2:
                m1 = 1
            else:
                m1 = 0
            m2 = (n - 2 * m1) // 3
            return 2**m1 * 3**m2

        # import math
        # if n == 2 or n == 3:
        #     return n - 1
        # else:
        #     x = n/math.e
        #     ans = 0
        #     for y in [math.floor(x), math.ceil(x)]:
        #         x1 = int(n/y)
        #         x2 = x1 + 1
        #         n2 = n - x1*y
        #         n1 = y - n2
        #         ans = max(ans, (x1**n1) * (x2**n2))
        #     return int(ans)
