s = input()
if s[0] == 'A':
    cnt = 0
    for i in range(2, len(s) - 1):
        if s[i] == 'C':
            cnt += 1
    if cnt == 1:
        s = list(s)
        s.remove('A')
        s.remove('C')
        a = ','.join(s)
        if a.islower() == True:
            print('AC')
        else:
            print('WA')
    else:
        print('WA')
else:
    print('WA')
