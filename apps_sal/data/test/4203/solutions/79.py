s = input()

if s[0] == 'A' and 'C' in s[2:-1] and all(elem == elem.lower() for i, elem in enumerate(s) if i != 0 and i != s.index('C')):
    print('AC')
else:
    print('WA')
