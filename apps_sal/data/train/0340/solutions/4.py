class Solution:

    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        place = [p for p in path.split('/') if p != '.' and p != '']
        stack = []
        for p in place:
            if p == '..':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(p)
        return '/' + '/'.join(stack)
