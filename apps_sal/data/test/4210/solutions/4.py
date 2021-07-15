n, k = map(int, input().split())
a = input().split()
mods = [dict() for i in range(10)]
l = [0] * n
for i in range(n):
    l[i] = len(a[i])
    a[i] = int(a[i]) % k
    cur = a[i]
    for j in range(10):
        cur = cur * 10 % k
        mods[j][cur] = mods[j].get(cur, 0) + 1
ans = 0
for i in range(n):
    mod = (k - a[i]) % k
    ans += mods[l[i] - 1].get(mod, 0)
    cur = a[i]
    for j in range(l[i]):
        cur = cur * 10 % k
    if cur == mod:
        ans -= 1
print(ans)
