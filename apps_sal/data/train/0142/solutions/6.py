class Solution:
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        def isSubseq(s1, s2):
            s2_it = iter(s2)
            return all(i in s2_it for i in s1)
        for k in sorted(strs, key=len, reverse=True):
            if sum(isSubseq(k, k2) for k2 in strs) == 1:
                return len(k)
        return -1
