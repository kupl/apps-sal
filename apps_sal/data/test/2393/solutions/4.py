n = int(input())
for i in range(n):
    x = input()
    bfx = x.split('twone')
    x = list(x)
    res = []
    if len(bfx) > 0:
        last = 0
        for g in range(len(bfx) - 1):
            res.append(last + len(bfx[g]) + 3)
            last += len(bfx[g]) + 5
        x = list('tw-ne'.join(bfx))
    for g in range(len(x) - 2):
        if x[g:g + 3] == ['o', 'n', 'e'] or x[g:g + 3] == ['t', 'w', 'o']:
            x[g + 1] = '-'
            res.append(g + 2)
    print(len(res))
    print(*res)
