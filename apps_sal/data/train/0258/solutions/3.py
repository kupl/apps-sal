class Solution:
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """

        res = ""
        res += "0" * s.count('z')
        res += "1" * (s.count('o') - s.count('z') - s.count('w') - s.count('u'))
        res += "2" * s.count('w')
        res += "3" * (s.count('h') - s.count('g'))
        res += "4" * s.count('u')
        res += "5" * (s.count('f') - s.count('u'))
        res += "6" * s.count('x')
        res += "7" * (s.count('s') - s.count('x'))
        res += "8" * s.count("g")
        res += "9" * (s.count('i') - s.count('x') - s.count("g") - s.count('f') + s.count('u'))
        return res

        """
    #    my solution..........beat 68%....
         from collections import Counter
         dic = Counter(s)
         res = {0:'', 1:'', 2:'', 3:'', 4:'', 5:'', 6:'', 7:'', 8:'', 9:''}
         
         if dic['z'] != 0:
             res[0] = '0'*dic['z']
             s = s.replace('z', '', dic['z'])
             s = s.replace('e', '', dic['z'])
             s = s.replace('r', '', dic['z'])
             s = s.replace('o', '', dic['z'])
             dic['z'], dic['e'], dic['r'], dic['o'] = 0, dic['e']-dic['z'], dic['r']-dic['z'], dic['o']-dic['z']
             
         if dic['w'] != 0:
             res[2] = '2'*dic['w']
             s = s.replace('t', '', dic['w'])
             s = s.replace('w', '', dic['w'])
             s = s.replace('o', '', dic['w'])
             dic['t'], dic['w'], dic['o'] = dic['t']-dic['w'], 0, dic['o']-dic['w']
             
         if dic['u'] != 0:
             res[4] = '4'*dic['u']
             s = s.replace('f', '', dic['u'])
             s = s.replace('o', '', dic['u'])
             s = s.replace('u', '', dic['u'])
             s = s.replace('r', '', dic['u'])
             dic['f'], dic['o'], dic['u'], dic['r'] = dic['f']-dic['u'], dic['o']-dic['u'], 0, dic['r']-dic['u']
             
         if dic['x'] != 0:
             res[6] = '6'*dic['x']
             s = s.replace('s', '', dic['x'])
             s = s.replace('i', '', dic['x'])
             s = s.replace('x', '', dic['x'])
             dic['s'], dic['i'], dic['x'] = dic['s']-dic['x'], dic['i']-dic['x'], 0
             
         if dic['g'] != 0:
             res[8] = '8'*dic['g']
             s = s.replace('e', '', dic['g'])
             s = s.replace('i', '', dic['g'])
             s = s.replace('g', '', dic['g'])
             s = s.replace('h', '', dic['g'])
             s = s.replace('t', '', dic['g'])
             dic['e'], dic['i'], dic['g'], dic['h'], dic['t'] = dic['e']-dic['g'], dic['i']-dic['g'], 0, dic['h']-dic['g'], dic['t']-dic['g']
 
             
         if dic['s'] != 0:
             res[7] = '7'*dic['s']
             s = s.replace('s', '', dic['s'])
             s = s.replace('e', '', 2*dic['s'])
             s = s.replace('v', '', dic['s'])
             s = s.replace('n', '', dic['s'])            
             dic['s'], dic['e'], dic['v'], dic['n'] = 0, dic['e']-2*dic['s'], dic['v']-dic['s'], dic['n']-dic['s']
             
         if dic['r'] != 0:
             res[3] = '3'*dic['r']
             s = s.replace('t', '', dic['r'])
             s = s.replace('h', '', dic['r'])
             s = s.replace('r', '', dic['r'])
             s = s.replace('e', '', 2*dic['r'])
             dic['t'], dic['h'], dic['r'], dic['e'] = dic['t']-dic['r'], dic['h']-dic['r'], 0, dic['e']-2*dic['r']
         
         if dic['v'] != 0:
             res[5] = '5'*dic['v']
             s = s.replace('f', '', dic['v'])
             s = s.replace('i', '', dic['v'])
             s = s.replace('v', '', dic['v'])
             s = s.replace('e', '', dic['v'])
             dic['f'], dic['i'], dic['v'], dic['e'] = dic['f']-dic['v'], dic['i']-dic['v'], 0, dic['e']-dic['v']
             
         if dic['i'] != 0:
             res[9] = '9'*dic['i']
             s = s.replace('n', '', 2*dic['i'])
             s = s.replace('i', '', dic['i'])
             s = s.replace('e', '', dic['i'])
             dic['n'], dic['i'], dic['e'] = dic['n']-2*dic['i'], 0, dic['e']-dic['i']
             
         if dic['n'] != 0:
             res[1] = '1'*dic['n']
             s = s.replace('o', '', dic['n'])
             s = s.replace('n', '', dic['n'])
             s = s.replace('e', '', dic['n'])
             dic['o'], dic['n'], dic['e'] = dic['o']-dic['n'], 0, dic['e']-dic['n']
             
         return res[0]+res[1]+res[2]+res[3]+res[4]+res[5]+res[6]+res[7]+res[8]+res[9]
         """
