n, m = map(int, input().split())
lm = list(map(int, input().split()))

impossible = False
an = [-1] * (n + 1)
f = [False] * (n + 1)
for k in range(m - 1):
    if an[lm[k]] < 0:
        for i in range(1, n + 1):
            if f[i]:
                continue
            x = lm[k] + i
            if x > n:
                x -= n
            if lm[k + 1] != x:
                continue
            an[lm[k]] = i
            f[i] = True
            break
        if an[lm[k]] < 0:
            impossible = True
            break
    else:
        x = lm[k] + an[lm[k]]
        if x > n:
            x -= n
        if lm[k + 1] != x:
            impossible = True
            break

if impossible:
    print(-1)
else:
    for i in range(1, n + 1):
        if an[i] > 0:
            continue
        for j in range(1, n + 1):
            if f[j]:
                continue
            an[i] = j
            f[j] = True
            break
    print(*an[1:])
