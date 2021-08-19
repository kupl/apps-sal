class Solution:

    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        p = []
        for i in range(1, 5):
            p.append(eval('p' + str(i)))
        e = {}
        for i in range(4):
            for j in range(4):
                for k in range(j + 1, 4):
                    if i == j or i == k or j == k:
                        continue
                    dij = (p[i][0] - p[j][0]) ** 2 + (p[i][1] - p[j][1]) ** 2
                    dik = (p[i][0] - p[k][0]) ** 2 + (p[i][1] - p[k][1]) ** 2
                    djk = (p[j][0] - p[k][0]) ** 2 + (p[j][1] - p[k][1]) ** 2
                    if dij == dik and dij + dik == djk:
                        if dij in e:
                            e[dij] += 1
                        else:
                            e[dij] = 1
        for k in e:
            print(e[k])
        if len(e) != 1:
            return False
        for k in e:
            if e[k] == 4:
                return True
            else:
                return False
