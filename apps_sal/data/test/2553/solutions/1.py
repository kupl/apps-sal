T = int(input())

for _ in range(T):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    p, q = 0, 0
    for i in a:
        if i % 2 == 0:
            p += 1
        else:
            q += 1
    ok = False
    for i in range(p + 1):
        j = x - i
        if j < 0 or j > q:
            continue
        if j % 2 == 1:
            ok = True
            break
    if ok:
        print('Yes')
    else:
        print('No')
