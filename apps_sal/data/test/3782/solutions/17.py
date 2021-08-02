n, k, q = map(int, input().split())
l = list(map(int, input().split()))
ans = 10**10
for i in range(n):
    x = l[i]
    tmp = []
    z = []
    for j in range(n):
        if l[j] >= x:
            tmp.append(l[j])
        if l[j] < x or j == n - 1:
            tmp.sort()
            if len(tmp) - k + 1 > 0:
                z += tmp[:len(tmp) - k + 1]
            tmp = []
    z.sort()
    if len(z) >= q:
        ans = min(ans, z[q - 1] - x)
print(ans)
