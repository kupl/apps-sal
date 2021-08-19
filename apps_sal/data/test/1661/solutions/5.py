(n, m) = map(int, input().split())
c = list(map(int, input().split()))
d = list(map(int, input().split()))
ci = 0
di = 0
ans = 0
for i in range(n):
    if di == m:
        break
    if d[di] >= c[i]:
        di += 1
        ans += 1
print(ans)
