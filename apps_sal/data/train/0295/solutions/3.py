class Solution:

    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        l = len(x)
        iscross = False
        if l < 4:
            return False
        for i in range(3, l):
            if x[i - 3] >= x[i - 1] and x[i - 2] <= x[i]:
                return True
            if i >= 4 and x[i - 4] + x[i] >= x[i - 2] and (x[i - 3] == x[i - 1]):
                return True
            if i >= 5 and x[i - 5] + x[i - 1] >= x[i - 3] and (x[i - 4] + x[i] >= x[i - 2]) and (x[i - 2] >= x[i - 4]) and (x[i - 2] > x[i - 4]) and (x[i - 3] > x[i - 5]) and (x[i - 1] < x[i - 3]):
                return True
            iscross = False
        return iscross
