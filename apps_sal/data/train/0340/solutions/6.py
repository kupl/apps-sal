class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        place = [p for p in path.split('/') if p != '.' and p != '']
        result = []
        for p in place:
            if p == '..':
                if len(result) > 0:
                    result.pop()
            else:
                result.append(p)
        return '/' + '/'.join(result)
