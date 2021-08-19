class Solution:

    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        l = [p1, p2, p3, p4]
        s = set()
        for i in range(len(l)):
            for j in range(i + 1, len(l)):
                d = self.dist(l[i], l[j])
                if d == 0:
                    return False
                s.add(d)
        return len(s) == 2

    def dist(self, a, b):
        return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
