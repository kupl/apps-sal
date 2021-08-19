def f(i):
    return (i + 1) % 3


for TT in range(1, int(input()) + 1):
    n = int(input())
    l = [*map(int, input().split())]
    s = ['RPS'.index(e) for e in input()]
    valid = True
    res = [-1] * n
    cnt = 0
    for (i, e) in enumerate(s):
        j = f(e)
        if l[j] > 0:
            l[j] -= 1
            res[i] = j
            cnt += 1
    j = 0
    for i in range(n):
        if res[i] != -1:
            continue
        while j < 3 and l[j] == 0:
            j += 1
        res[i] = j
        l[j] -= 1
    valid &= cnt >= (n + 1) // 2
    if valid:
        print('YES')
        print(''.join(('RPS'[e] for e in res)))
    else:
        print('NO')
