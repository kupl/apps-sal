class Solution:

    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """

        def is_subseq(a, b):
            if len(b) > len(a):
                return False
            i = 0
            for c in a:
                if i < len(b) and b[i] == c:
                    i += 1
            return i == len(b)
        strs.sort(key=lambda x: -len(x))
        for (i, s) in enumerate(strs):
            if not any((is_subseq(s2, s) for s2 in strs[:i])) and (not any((is_subseq(s2, s) for s2 in strs[i + 1:]))):
                return len(s)
        return -1
