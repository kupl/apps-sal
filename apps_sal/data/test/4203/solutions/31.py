S = input()

if S[0] == 'A':
    c = list(S[2:-1])
    if c.count('C') == 1:
        p = c.index('C')
        c.pop(p)
        ans = list(S[1]) + c + list(S[-1])
        anss = ''.join(ans)
        if anss.islower():
            print('AC')
        else:
            print('WA')
    else:
        print('WA')
else:
    print('WA')
