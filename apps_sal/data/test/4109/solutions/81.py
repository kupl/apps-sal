n, m, x = list(map(int, input().split()))
ll = [list(map(int, input().split())) for _ in range(n)]
ans = 10**9

for i in range(2**n):
    a = [0]*m
    cnt = 0
    for j in range(n):
        if i>>j & 1:
            for k in range(1, m+1):
                a[k-1] += ll[j][k]
            cnt += ll[j][0]
    if all(s >= x for s in a):
        ans = min(ans, cnt)
print((ans if ans < 10**9 else -1))

