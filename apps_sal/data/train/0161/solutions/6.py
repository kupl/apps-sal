class Solution:
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        if not preorder:
            return True
        arr = preorder.split(',')
        s = []
        for a in arr:
            s.append(a)
            while len(s) >= 3 and s[-1] == '#' and s[-2] == '#' and s[-3] != '#':
                s.pop()
                s.pop()
                s.pop()
                s.append('#')
        if s == ['#']:
            return True
        return False
