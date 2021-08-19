class Solution:

    def maxDiff(self, num: int) -> int:
        if num < 10:
            return 8
        numStr = str(num)
        (a, b) = ([], [])
        for i in range(len(numStr)):
            a.append(numStr[i])
            b.append(numStr[i])
        for i in range(len(a)):
            temp = a[i]
            if not a[i] == '9':
                for j in range(len(a)):
                    if a[j] == temp:
                        a[j] = '9'
                break
        for i in range(len(b)):
            if i == 0:
                temp = b[0]
                if not b[0] == '1':
                    for j in range(len(b)):
                        if b[j] == temp:
                            b[j] = '1'
                    break
            else:
                temp = b[i]
                if not b[i] == '0' and (not b[i] == '1'):
                    for j in range(len(b)):
                        if b[j] == temp:
                            b[j] = '0'
                    break
        (c, d) = ('', '')
        for i in range(len(numStr)):
            (c, d) = (c + a[i], d + b[i])
        return int(c) - int(d)
