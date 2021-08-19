class Solution:

    def dist(self, p1, p2):
        return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        ps = [p1, p2, p3, p4]
        ds = []
        for i in range(3):
            for j in range(i + 1, 4):
                ds.append(self.dist(ps[i], ps[j]))
        ds.sort()
        return ds[0] > 0 and ds[0] == ds[1] == ds[2] == ds[3] and (ds[4] == ds[5])
