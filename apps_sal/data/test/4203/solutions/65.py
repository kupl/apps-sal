s = input()
s_1 = s[2:-1]
s_2 = s.replace('A', 'a')
s_3 = s_2.replace('C', 'c')
if s[0] == 'A' and s_1.count('C') == 1 and (s_3 == s.lower()):
    print('AC')
else:
    print('WA')
