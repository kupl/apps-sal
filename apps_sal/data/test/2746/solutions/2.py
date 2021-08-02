class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        l1 = [int(x) for x in version1.split('.')]
        l2 = [int(x) for x in version2.split('.')]

        max_len = max(len(l1), len(l2))
        l1 += [0] * (max_len - len(l1))
        l2 += [0] * (max_len - len(l2))

        for i in range(0, max_len):
            if l1[i] > l2[i]:
                return 1
            elif l1[i] < l2[i]:
                return -1

        return 0
