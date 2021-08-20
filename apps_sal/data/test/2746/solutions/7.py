class Solution:

    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = [int(n) for n in version1.split('.')]
        v2 = [int(n) for n in version2.split('.')]
        for i in range(max(len(v1), len(v2))):
            x1 = v1[i] if i < len(v1) else 0
            x2 = v2[i] if i < len(v2) else 0
            if x1 > x2:
                return 1
            if x1 < x2:
                return -1
        return 0
