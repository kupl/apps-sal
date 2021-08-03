class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        tmpstr = ''
        path += '/'
        for c in path:
            if c == '/':
                if tmpstr:
                    if tmpstr == '..':
                        if stack:
                            stack.pop()
                    elif tmpstr != '.':
                        stack.append(tmpstr)
                tmpstr = ''
            else:
                tmpstr += c
        return '/' + "/".join(stack)
