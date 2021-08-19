n = int(input())
f = [input().split() for i in range(n)]
m = [False, False]
sl = list(map(int, input().split()))
if n == 1:
    print('YES')
else:
    if f[sl[0] - 1][0] <= f[sl[1] - 1][0] or f[sl[0] - 1][1] <= f[sl[1] - 1][0]:
        m[0] = True
    if f[sl[0] - 1][0] <= f[sl[1] - 1][1] or f[sl[0] - 1][1] <= f[sl[1] - 1][1]:
        m[1] = True
    (a, b) = (False, False)
    for i in range(1, n - 1):
        if m[0] and f[sl[i] - 1][0] <= f[sl[i + 1] - 1][0] or (m[1] and f[sl[i] - 1][1] <= f[sl[i + 1] - 1][0]):
            a = True
        else:
            a = False
        if m[0] and f[sl[i] - 1][0] <= f[sl[i + 1] - 1][1] or (m[1] and f[sl[i] - 1][1] <= f[sl[i + 1] - 1][1]):
            b = True
        else:
            b = False
        (m[0], m[1]) = (a, b)
    if not m[0] and (not m[1]):
        print('NO')
    else:
        print('YES')
