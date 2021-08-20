class Solution:

    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        "\n         # unique letter in nums: zero, two, four, six, eight\n         uniques = [['z', 'w', 'u', 'x', 'g'],\n                    ['zero', 'two', 'four', 'six', 'eight'],\n                    ['0', '2', '4', '6', '8']]\n         # then the leftover are: one, three, five, seven, nine\n         # the unique letter in each is: except nine\n         leftover = [['o', 't', 'f', 's'],\n                     ['one', 'three', 'five', 'seven'],\n                     ['1', '3', '5', '7']]\n         res = ''\n         count = collections.Counter(s)\n         for l in uniques[0]:\n             cntl = count[l]\n             if cntl != 0:\n                 idx = uniques[0].index(l)\n                 res += uniques[2][idx]*cntl\n                 for m in uniques[1][idx]:\n                     s = s.replace(m, '', cntl)\n                     count[m] -= cntl\n         #return s\n         for l in leftover[0]:\n             cntl = count[l]\n             if cntl != 0:\n                 idx = leftover[0].index(l)\n                 res += leftover[2][idx]*cntl\n                 for m in leftover[1][idx]:\n                     s = s.replace(m, '', cntl)\n                     count[m] -= cntl\n         res += '9'*count['i']\n         return ''.join(letter for letter in sorted(res))\n         "
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
        return ''.join((letter for letter in sorted(tmp)))
