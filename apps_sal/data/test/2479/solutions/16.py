(n, q) = map(int, input().split())
ans = (n - 2) ** 2
h = n - 2
r = n - 2
l_h = [-1] * (n - 2)
l_r = [-1] * (n - 2)
for _ in range(q):
    (a, x) = map(int, input().split())
    if a == 1:
        if x - 1 > r:
            ans -= l_r[x - 2]
        else:
            r = x - 2
            ans -= h
            for i in range(x - 1, n - 2):
                if l_r[i] == -1:
                    l_r[i] = h
                else:
                    break
    elif x - 1 > h:
        ans -= l_h[x - 2]
    else:
        h = x - 2
        ans -= r
        for i in range(x - 1, n - 2):
            if l_h[i] == -1:
                l_h[i] = r
            else:
                break
print(ans)
