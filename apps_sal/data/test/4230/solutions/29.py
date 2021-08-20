(X, N) = (int(x) for x in input().split())
p = sorted(list((int(x) for x in input().split())))
if N == 0:
    print(X)
elif N == 1:
    if p[0] == X:
        print(X - 1)
    else:
        print(X)
else:
    ans = float('inf')
    for z in range(0, p[0]):
        if (ans - X) ** 2 > (z - X) ** 2:
            ans = z
    for i in range(N - 1):
        for z in range(p[i] + 1, p[i + 1]):
            if (ans - X) ** 2 > (z - X) ** 2:
                ans = z
    for z in range(p[-1] + 1, 102):
        if (ans - X) ** 2 > (z - X) ** 2:
            ans = z
    print(ans)
