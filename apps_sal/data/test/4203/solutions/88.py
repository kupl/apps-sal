s = input()
if s[1] != 'C' and s[2:-1].count('C') == 1 and (s[-1] != 'C') and (s[0] == 'A') and s[1:s.find('C')].islower() and s[s.find('C') + 1:].islower():
    print('AC')
else:
    print('WA')
