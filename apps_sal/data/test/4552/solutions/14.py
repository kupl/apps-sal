n = int(input())
f = []
for i in range(n):
    fn = [int(x) for x in input().rstrip().split()]
    f.append(fn)
p = []
for i in range(n):
    pn = [int(x) for x in input().rstrip().split()]
    p.append(pn)
ans = -float('inf')
for i in range(1, 2 ** 10):
    now = 0
    for s in range(n):
        cnt = 0
        for j in range(10):
            if i >> j & 1 and f[s][j] == 1:
                cnt += 1
        now += p[s][cnt]
    ans = max(ans, now)
print(ans)
