n, x, m = map(int, input().split())
a = []
mp = dict()
cnt, tot = 0, 0
while mp.get(x, -1) == -1:
    a.append(x)
    tot += x
    mp[x] = cnt
    cnt += 1
    x = (x * x) % m

if n <= cnt:
    ans = 0
    for i in range(0, n): ans += a[i]
    print(ans)
    return
cycle = 0
rest = cnt - mp.get(x, 0)
for i in range(mp[x], cnt):
    cycle += a[i]
n-= cnt
ans = tot
ans += (n // rest) * cycle
n %= rest
si = mp.get(x, 0)
for i in range(n): ans += a[si + i]
print(int(ans))
