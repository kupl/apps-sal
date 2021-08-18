class Solution:
    def findIntegers(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 3:
            return num + 1
        if num == 3:
            return num
        import math
        bits = int(math.log(num, 2))
        f = [0] * (bits + 1)
        f[0], f[1], f[2] = 2, 3, 4
        for i in range(3, bits + 1):
            f[i] = f[i - 1] + f[i - 2] - 1

        g = [0] * (bits + 1)
        n = num
        b = 0
        res = [0] * (bits + 1)
        while n:
            cur = n % 2
            g[b] = cur
            if cur:
                if not b:
                    res[b] = f[b]
                elif not res[b - 1]:
                    res[b] = f[b] + res[b - 1]

                elif not g[b - 1]:
                    res[b] = f[b] + res[b - 1] - 1
                else:
                    res[b] = f[b] + f[b - 1] - 2

            else:
                res[b] = res[b - 1]
            n = int(n / 2)
            b = b + 1
        return res[-1]
