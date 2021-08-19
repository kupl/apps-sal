class Solution:

    def flipLights(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        n = min(n, 3)
        if n == 0:
            return 0
        if n == 1:
            return 2 if m > 0 else 1
        if n == 2:
            if m == 0:
                return 1
            elif m == 1:
                return 3
            else:
                return 4
        if n == 3:
            if m == 0:
                return 1
            elif m == 1:
                return 4
            elif m == 2:
                return 7
            else:
                return 8
