class Solution:
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """

        dir = []
        tab = 0
        curr = []
        temp = ''
        op = 0
        input += '\n'
        for c in input:
            print('start:', c, temp)
            if c == '\n' and temp != '':
                if curr:
                    print(curr)
                    while tab <= curr[-1]:
                        dir.pop(-1)
                        curr.pop(-1)
                        if not curr:
                            break
                dir.append(temp)
                curr.append(tab)
                print(dir, curr)
                if '.' in temp:
                    ans = '/'.join(dir)
                    op = max(len(ans), op)
                temp = ''
                tab = 0
            elif c == '\t':
                tab += 1
            else:
                temp += c

        return op
