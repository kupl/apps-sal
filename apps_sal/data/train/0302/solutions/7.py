class Solution:

    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        ps = sorted([p1, p2, p3, p4])
        return ps[0][0] + ps[3][0] == ps[1][0] + ps[2][0] and ps[0][1] + ps[3][1] == ps[1][1] + ps[2][1] and (ps[2][0] - ps[1][0] == abs(ps[3][1] - ps[0][1])) and (not ps[0] == ps[1])
