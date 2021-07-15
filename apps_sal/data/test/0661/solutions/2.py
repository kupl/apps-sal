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
        l = list(range(2 ** m))
        l.pop(k)
        ans = l + [k] + l[::-1] + [k]
        print((' '.join(map(str, ans))))
    else:
        print((-1))


