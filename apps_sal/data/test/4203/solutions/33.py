s = input()
if len(s) < 4:
    print('WA')
elif s[0] != 'A':
    print('WA')
elif s[2:-1].count('C') != 1:
    print('WA')
else:
    tmp = s[1] + s[2:].replace('C', 'c')
    if tmp != tmp.lower():
        print('WA')
    else:
        print('AC')
