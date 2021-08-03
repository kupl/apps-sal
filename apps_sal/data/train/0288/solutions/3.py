class Solution:
    def flipLights(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        if n == 0:
            return 0
        if m == 0:
            return 1
        if n == 1:
            return 2
        if n == 2:
            if m >= 2:
                return 4
            if m == 1:
                return 3
        if n >= 3:
            if m >= 3:
                return 8
            if m == 2:
                return 7
            if m == 1:
                return 4
