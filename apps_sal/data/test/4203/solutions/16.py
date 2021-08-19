s = list(map(str, input()))
if s[0] != 'A':
    print('WA')
elif s[2:-1].count('C') != 1:
    print('WA')
else:
    del s[0]
    s.remove('C')
    if ''.join(s).islower():
        print('AC')
    else:
        print('WA')
