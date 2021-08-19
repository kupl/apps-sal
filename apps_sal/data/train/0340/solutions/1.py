class Solution:

    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        res = []
        str_list = path.split('/')
        loc = len(str_list) - 1
        for i in range(len(str_list)):
            ss = str_list[i]
            if ss == '':
                continue
            if ss == '.':
                continue
            if ss == '..':
                if len(res) > 0:
                    res.pop()
            else:
                res.append(ss)
        return '/' + '/'.join(res)
