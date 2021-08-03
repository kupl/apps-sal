class Solution:
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        def distance(m1, m2):
            x1 = m1[0]
            y1 = m1[1]
            x2 = m2[0]
            y2 = m2[1]
            return (((y2 - y1)**2) + ((x2 - x1)**2))**0.5

        m = [d1, d2, d3, d4, d5, d6] = distance(p1, p2), distance(p2, p3), distance(p3, p4), distance(p4, p1), distance(p2, p4), distance(p3, p1)
        m = sorted(list(m))
        print(m)
        c = 0
        x = m[0]
        if m[0] == 0.0 and m[1] == 0.0 and m[2] == 0.0 and m[3] == 0.0:
            return False
        for i in m:
            if c == 4:
                return True
            if i == m[0]:
                c += 1
            else:
                m[0] = i
                c = 0
        return False
