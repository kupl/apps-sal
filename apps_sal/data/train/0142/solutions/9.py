class Solution:
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        def isSubsequence(a, b):
            i = 0
            j = 0
            while i < len(a) and j < len(b):
                if j == len(b) - 1 and (i < len(a) - 1 or a[i] != b[j]):
                    return False
                if a[i] != b[j]:
                    j += 1
                else:
                    i += 1
                    j += 1
            return True
        flag = 0
        l = []
        for i in range(len(strs)):
            for j in range(len(strs)):
                if i != j and isSubsequence(strs[i], strs[j]):
                    flag = 1
                    break
            if flag == 0:
                l.append(strs[i])
            flag = 0
        if l == []:
            return -1
        res = max(list([len(x) for x in l]))
        return res
