class Solution:

    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """

        def length(x, y):
            return (x[0] - y[0]) * (x[0] - y[0]) + (x[1] - y[1]) * (x[1] - y[1])
        res = []
        a1 = length(p1, p2)
        a2 = length(p1, p3)
        a3 = length(p1, p4)
        a4 = length(p2, p3)
        a5 = length(p2, p4)
        a6 = length(p3, p4)
        res = [a1, a2, a3, a4, a5, a6]
        res = sorted(res)
        for i in range(3):
            if res[i] == res[i + 1]:
                continue
            else:
                return False
        if res[4] != res[5]:
            return False
        if res[0] != 0:
            return True
        else:
            return False
