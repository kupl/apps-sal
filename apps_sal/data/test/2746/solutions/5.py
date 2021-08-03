class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        a, b = [int(i) for i in version1.split('.')], [int(i) for i in version2.split('.')]
        for i in range(max(len(a), len(b))):
            if i == len(a):
                a.append(0)
            if i == len(b):
                b.append(0)
            if a[i] > b[i]:
                return 1
            elif a[i] < b[i]:
                return -1
        return 0
