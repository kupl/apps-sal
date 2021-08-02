import math

t = int(input())

for f in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    cnt = [0] * n

    for i in range(n):
        cnt[i] = b[i] - a[i]

    u = [True] * n
    l, r = 0, 0
    for i in range(n):
        if cnt[i] != 0:
            l = i
            break
    for i in range(n - 1, -1, -1):
        if cnt[i] != 0:
            r = i
            break

    el = cnt[l]
    ans = True
    for i in range(l, r + 1):
        if cnt[i] != el or cnt[i] < 0:
            ans = False

    if ans:
        print('YES')
    else:
        print('NO')
