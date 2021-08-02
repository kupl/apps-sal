m, k = list(map(int, input().split()))

if m == 0:
    if k == 0:
        print('0 0')
    else:
        print('-1')
elif m == 1:
    if k == 0:
        print('0 0 1 1')
    elif k >= 1:
        print('-1')
else:
    if k < 2 ** m:
        l = []
        for i in range(2 ** m):
            if i != k:
                l.append(i)

        ans = l + [k] + l[::-1] + [k]

        ans2 = ''
        for a in ans:
            ans2 += str(a) + ' '
        print((ans2[:-1]))
    else:
        print((-1))
