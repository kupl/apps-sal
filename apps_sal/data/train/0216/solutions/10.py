class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        neighcount = [0, 0, 0, 0, 0]
        minhorses = 0
        nstarted = 0
        nended = 0

        for s in croakOfFrogs:
            if s == 'c':
                neighcount[0] += 1
                nstarted += 1
            elif s == 'r':
                neighcount[1] += 1
                neighcount[0] -= 1
            elif s == 'o':
                neighcount[2] += 1
                neighcount[1] -= 1
            elif s == 'a':
                neighcount[3] += 1
                neighcount[2] -= 1
            elif s == 'k':
                neighcount[4] += 1
                neighcount[3] -= 1
                nstarted -= 1
            else:
                return -1
            if nstarted > minhorses:
                minhorses = nstarted
            if neighcount[0] < 0 or neighcount[1] < 0 or neighcount[2] < 0 or neighcount[3] < 0:
                return -1
        if neighcount[0] == 0 and neighcount[1] == 0 and neighcount[2] == 0 and neighcount[3] == 0:
            return minhorses
        else:
            return -1
