s = input()
l = []
for i in s:
    l.append(i)
if l[0] != 'A':
    print('WA')
elif len(l) == 3:
    if l[1].islower() and l[2] == 'C':
        print('AC')
    else:
        print('WA')
else:
    l.remove('A')
    if 'C' not in l[1:len(l) - 1]:
        print('WA')
    else:
        l.remove('C')
        s = ''.join(l)
        if s.islower():
            print('AC')
        else:
            print('WA')
