t = int(input())
for j in range(t):
    e = input()
    m, k = map(int, input().split())
    arr = [int(i) for i in input().split()]
    sum, bfail = [0] * k, [0] * k
    ffail, undef = -1, 0
    used = [False] * k
    ubfail = 0
    for i in range(m - 1):
        c, ns = map(int, input().split())
        if c == 0:
            undef += 1
            if ns == 0 and ffail == -1:
                ubfail += 1
        else:
            sum[c - 1] += 1
            if ns == 0 and ffail == -1:
                bfail[c - 1] += 1
        if ns and ffail == -1:
            ffail = i
        if ffail != -1 and c > 0:
            used[c - 1] = True
    if ffail == -1:
        for i in range(k):
            if sum[i] + undef >= arr[i]:
                print('Y', end = '')
            else:
                print('N', end = '')
        print()
        continue
    minu = 10 ** 6
    for i in range(k):
        if not used[i] and arr[i] - bfail[i] < minu:
            minu = arr[i] - bfail[i]
            best = i
    for i in range(k):
        if i == best or undef - minu + sum[i] >= arr[i]:
            print('Y', end = '')
        elif bfail[i] + ubfail >= arr[i] and not used[i]:
            print('Y', end = '')
        else:
            print('N', end = '')
    print()

