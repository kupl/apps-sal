s = input()
if s[0] == 'A' and s[2:-1].count('C') == 1 and s[-1].islower():
    ind = s.index('C')
    if s[1:ind].islower() and (ind == len(s) - 2 or s[ind + 1:-1].islower()):
        print('AC')
        return
print('WA')
