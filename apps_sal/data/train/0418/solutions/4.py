class Solution:
    def Is2(self, n):
        root = int(math.log(n, 2))
        return (2**root) == n

    def GetNear2(self, n):
        if n == 0:
            return -1
        if n == 1:
            return 0
        if n == 2:
            return 1
        if self.Is2(n):
            return n
        for ind in range(n - 1, n + 2):
            if self.Is2(ind):
                return ind
        return -1

    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """

        m = n
        cnt = 0
        while m != 1:
            if m == 1:
                return cnt
            if m == 2:
                return 1 + cnt
            if m <= 4:
                return 2 + cnt
            if m <= 6:
                return 3 + cnt
            if m % 2 == 0:
                cnt += 1
                m = int(m / 2)
                continue
            k = m % 4
            if k == 1:
                cnt += 1
                m = int(m - 1)
            elif k == 3:
                cnt += 1
                m = int(m + 1)

        return cnt
