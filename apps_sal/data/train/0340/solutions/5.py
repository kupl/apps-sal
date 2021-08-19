class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        l = []
        ans = '/'
        names = path.split('/')
        print(('names', names))
        for s in names:
            if s == '..':
                # if len(l) == 0:
                #     l.append(s)
                # else:
                #     l.pop()
                if len(l) != 0:
                    l.pop()
            elif s == '.':
                continue
            elif s == '':
                continue
            else:
                l.append(s)
        print(('l: ', l))
        for s in l:
            ans += s + '/'
        n = len(ans)
        if n > 1:
            return ans[:len(ans) - 1]
        else:
            return ans
