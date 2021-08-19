(n, m) = map(int, input().split())
all = [0 for i in range(m)]
ans = 0
for i in range(n):
    p = list(map(int, input().split()))
    last = p[0] + 1
    for l in range(1, last):
        all[p[l] - 1] += 1
for i in all:
    if i == n:
        ans += 1
print(ans)
