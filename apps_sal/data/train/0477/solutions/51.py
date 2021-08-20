class Solution:

    def findKthBit(self, n: int, k: int) -> str:
        s = []
        for i in range(n):
            if i == 0:
                s.append(['0'])
            else:
                temp = s[i - 1].copy()
                for j in range(len(temp)):
                    if temp[j] == '0':
                        temp[j] = '1'
                    else:
                        temp[j] = '0'
                temp = temp[::-1]
                s.append([])
                for zz in s[i - 1]:
                    s[i].append(zz)
                s[i].append('1')
                for zz in temp:
                    s[i].append(zz)
        return s[-1][k - 1]
