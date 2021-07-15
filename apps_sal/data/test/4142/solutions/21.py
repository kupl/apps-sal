s = input()
s1 = set(s[::2]) - set('RUD')
s2 = set(s[1::2]) - set('LUD')
if s1 or s2:
    print('No')
else:
    print('Yes')
