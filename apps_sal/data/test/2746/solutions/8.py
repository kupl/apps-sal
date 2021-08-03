from itertools import zip_longest


class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        rs = None
        for x in zip_longest(
                (int(x) for x in version1.split('.')),
                (int(x) for x in version2.split('.')),
                fillvalue=0):
            if x[0] == x[1]:
                pass
            else:
                rs = x[0] > x[1]
                break

        return {None: 0, True: 1, False: -1}[rs]
