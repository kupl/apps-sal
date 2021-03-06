class Solution:

    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        pc = None
        sl = 0
        ll = {}
        for c in p:
            if pc and (ord(pc) + 1 == ord(c) or (pc == 'z' and c == 'a')):
                sl += 1
            else:
                sl = 1
            ll[c] = max([ll[c], sl]) if c in ll else sl
            pc = c
        s = 0
        for (key, value) in list(ll.items()):
            s += value
        return s
