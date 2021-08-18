n, x, m = list(map(int, input().split()))
ls = [-1] * (m + 1)
a = []
tot = 0
cnt = 0
while ls[x] == -1:
    a.append(x)
    tot += x
    ls[x] = cnt
    cnt += 1
    x = (x * x) % m

if n <= cnt:
    ans = 0
    for i in range(n):
        ans += a[i]
    print(ans)
    return
cycle = 0
rest = cnt - ls[x]
for i in range(ls[x], cnt):
    cycle += a[i]
n -= cnt
ans = tot
ans += (n // rest) * cycle
n %= rest
si = ls[x]
for i in range(n):
    ans += a[si + i]
print(ans)
