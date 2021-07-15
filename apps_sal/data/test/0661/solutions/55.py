m, k = [int(x) for x in input().split()]
if m == 1:
    if k == 0:
        print(0, 0, 1, 1)
    else:
        print(-1)
else:
    if k < 1 << m:
        a = [str(i) for i in range(1 << m) if i != k]
        print(' '.join(a), k, ' '.join(reversed(a)), k)
    else:
        print(-1)
