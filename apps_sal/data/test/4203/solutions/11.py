s = list(input())
al = list('abcdefghijklmnopqrstuvwxyz')
if s[0] == 'A' and s[-1] in al and (s[1] in al):
    del s[0]
    del s[0]
    del s[-1]
    f = 0
    for i in s:
        if i == 'C':
            if f == 1:
                print('WA')
                break
            else:
                f = 1
                continue
        elif i in al:
            continue
        else:
            print('WA')
            break
    else:
        if f == 1:
            print('AC')
        else:
            print('WA')
else:
    print('WA')
