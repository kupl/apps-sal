class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split(".")
        v2 = version2.split(".")
        for i in range(max(len(v1), len(v2))):
            a = int(v1[i]) if len(v1) > i else 0
            b = int(v2[i]) if len(v2) > i else 0
            if a > b:
                return 1
            elif a < b:
                return -1
        return 0
