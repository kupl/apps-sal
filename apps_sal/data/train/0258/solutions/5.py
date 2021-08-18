class Solution:
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        '''
         uniques = [['z', 'w', 'u', 'x', 'g'],
                    ['zero', 'two', 'four', 'six', 'eight'],
                    ['0', '2', '4', '6', '8']]
         leftover = [['o', 't', 'f', 's'],
                     ['one', 'three', 'five', 'seven'],
                     ['1', '3', '5', '7']]
         res = ''
         count = collections.Counter(s)
         for l in uniques[0]:
             cntl = count[l]
             if cntl != 0:
                 idx = uniques[0].index(l)
                 res += uniques[2][idx]*cntl
                 for m in uniques[1][idx]:
                     s = s.replace(m, '', cntl)
                     count[m] -= cntl
         for l in leftover[0]:
             cntl = count[l]
             if cntl != 0:
                 idx = leftover[0].index(l)
                 res += leftover[2][idx]*cntl
                 for m in leftover[1][idx]:
                     s = s.replace(m, '', cntl)
                     count[m] -= cntl
         res += '9'*count['i']
         return ''.join(letter for letter in sorted(res))
         '''
        dump = dict()
        dump[0] = s.count('z')
        dump[2] = s.count('w')
        dump[4] = s.count('u')
        dump[6] = s.count('x')
        dump[8] = s.count('g')
        dump[5] = s.count('f') - dump[4]
        dump[7] = s.count('s') - dump[6]
        dump[3] = s.count('h') - dump[8]
        dump[1] = s.count('o') - dump[0] - dump[2] - dump[4]
        dump[9] = s.count('i') - dump[5] - dump[6] - dump[8]
        tmp = ''
        for i in range(10):
            tmp += str(i) * dump[i]
        return ''.join(letter for letter in sorted(tmp))
