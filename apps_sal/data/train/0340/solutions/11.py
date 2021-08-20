class Solution:

    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        places = [tmp for tmp in path.split('/') if tmp != '.' and tmp != '']
        stack = []
        for name in places:
            if name == '.' or name == '':
                continue
            elif name == '..':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(name)
        return '/' + '/'.join(stack)
