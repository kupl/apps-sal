class Solution:
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        dmap = {}
        dmap[0] = s.count('z')
        dmap[2] = s.count('w')
        dmap[4] = s.count('u')
        dmap[6] = s.count('x')
        dmap[8] = s.count('g')
        dmap[1] = s.count('o') - dmap[0] - dmap[2] - dmap[4]
        dmap[3] = s.count('h') - dmap[8]
        dmap[5] = s.count('f') - dmap[4]
        dmap[7] = s.count('s') - dmap[6]
        dmap[9] = s.count('i') - dmap[6] - dmap[8] - dmap[5]
        res = ''
        dmap = sorted(list(dmap.items()), key=lambda x: x[0])
        lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        '''
         lst=['zero','one','two','three','four','five',
              'six','seven','eight','nine']
         这个是错误示范 我们需要输出的是数字 字符串 而不是字母
         '''
        for i in range(len(lst)):
            res += lst[i] * dmap[i][1]
        return res
