n = int(input())
x = list(map(int, input().split()))
mn = 0
mx = 0
minv = min(x)
maxv = max(x)
for i in x:
    if i == minv:
        mn += 1
    elif i == maxv:
        mx += 1
if minv != maxv - 2:
    print(n)
    for i in x:
        print(i, end=' ')
else:
    c = min(mn, mx)
    print(min((n - 2 * c), (mn + mx + (n - mn - mx) % 2)))
    if (n - 2 * c) < (mn + mx + (n - mn - mx) % 2):
        for i in range(len(x)):
            if (x[i] == maxv) and (c > 0):
                x[i] = (maxv + minv) // 2
                c -= 1
        c = min(mn, mx)
        for i in range(len(x)):
            if (x[i] == minv) and (c > 0):
                x[i] = (maxv + minv) // 2
                c -= 1
        for i in x:
            print(i, end=' ')
    else:
        c = (n - mn - mx) // 2
        for i in range(len(x)):
            if (x[i] == (minv + maxv) // 2) and (c > 0):
                c -= 1
                x[i] = minv
        c = (n - mn - mx) // 2
        for i in range(len(x)):
            if (x[i] == (minv + maxv) // 2) and (c > 0):
                c -= 1
                x[i] = maxv
        for i in x:
            print(i, end=' ')
