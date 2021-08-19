(n, m) = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
lim = sum(a) / (4 * m)
for i in a:
    if i >= lim:
        ans += 1
if ans >= m:
    print('Yes')
else:
    print('No')
