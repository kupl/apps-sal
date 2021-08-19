MOD = 10 ** 9 + 7


def I():
    return list(map(int, input().split()))


(t,) = I()
while t:
    t -= 1
    (n,) = I()
    a = [2] * n
    l = []
    for i in range(n):
        l.append(I() + [i])
    l.sort()
    mn = l[0][0]
    mx = l[0][1]
    i = 0
    while i < n and l[i][0] <= mx:
        mx = max(mx, l[i][1])
        a[l[i][2]] = 1
        i += 1
    if all([i == 1 for i in a]) or all([i == 2 for i in a]):
        print(-1)
    else:
        print(*a)
