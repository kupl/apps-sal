n, k = map(int, input().split())
a = [int(x) for x in input().split()]

ans = []
for i in range(n):
    c = 0
    imin = max(0, i - k)
    imax = min(n - 1, i + k)
    if a[i] != 0:
        c += ans[a[i] - 1]
        amin = max(0, a[i] - 1 - k)
        amax = min(n - 1, a[i] - 1 + k)
        if imin > amax:
            c += imax - imin + 1
        else:
            c += imax - amax
    else:
        c += imax - imin + 1
    ans.append(c)

print(" ".join([str(x) for x in ans]))
