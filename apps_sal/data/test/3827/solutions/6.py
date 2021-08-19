import re
pattern = '^a+b+c+$'
s = input()
if re.match(pattern, s):
    l = len(s)
    pos_b = s.index('b')
    pos_c = s.index('c')
    len_c = l - pos_c
    len_b = l - len_c - pos_b
    len_a = l - len_c - len_b
    print(('NO', 'YES')[len_c in (len_b, len_a)])
else:
    print('NO')
