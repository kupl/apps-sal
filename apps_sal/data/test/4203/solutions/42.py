s = input()
if s[0] == 'A':
    sub = s[2:-1]
    if sub.count('C') == 1:
        if all(c.islower() for c in s[1:].replace('C','')):
            print('AC')
            return

print('WA')
