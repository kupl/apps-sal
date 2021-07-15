s = list(input())
if len(s) % 2 == 0:
    s1 = s[0 : len(s) // 2 : ]
    s2 = s[len(s) // 2 : len(s) : ]
else:
    s1 = s[0 : len(s) // 2 + 1 : ]
    s2 = s[len(s) // 2 : len(s) : ]
s2.reverse()
d = dict()
d['A'] = 'A'
d['b'] = 'd'
d['d'] = 'b'
d['H'] = 'H'
d['I'] = 'I'
d['M'] = 'M'
d['O'] = 'O'
d['o'] = 'o'
d['T'] = 'T'
d['U'] = 'U'
d['V'] = 'V'
d['v'] = 'v'
d['W'] = 'W'
d['w'] = 'w'
d['X'] = 'X'
d['x'] = 'x'
d['Y'] = 'Y'
d['p'] = 'q'
d['q'] = 'p'
f = True
for i in range(len(s1)):
   if not(s1[i] in d and d[s1[i]] == s2[i]):
       f = False
       break
if f:
    print('TAK')
else:
    print('NIE')

