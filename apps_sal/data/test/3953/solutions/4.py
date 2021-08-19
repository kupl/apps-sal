n = int(input())
t = [input() for i in range(n)]
e = 'E' * n
if e in t:
    t = list((''.join(i) for i in zip(*t)))
    if e in t:
        print('-1')
    else:
        p = [str(c.find('.') + 1) + ' ' + str(i) for (i, c) in enumerate(t, 1)]
        print('\n'.join(p))
else:
    p = [str(i) + ' ' + str(c.find('.') + 1) for (i, c) in enumerate(t, 1)]
    print('\n'.join(p))
