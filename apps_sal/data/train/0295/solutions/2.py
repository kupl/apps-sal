class Solution:

    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        n = len(x)
        if n < 4:
            return False
        i = 3
        while i < n:
            if x[i] >= x[i - 2] and x[i - 3] >= x[i - 1]:
                return True
            if i >= 4:
                if x[i - 1] == x[i - 3] and x[i] + x[i - 4] >= x[i - 2]:
                    return True
            if i >= 5:
                if x[i] >= x[i - 2] - x[i - 4] >= 0 and x[i - 5] >= x[i - 3] - x[i - 1] >= 0:
                    return True
            i += 1
        return False
