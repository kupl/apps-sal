n, k = map(int, input().split())
a = list(map(int, input().split()))
sz = []
t = [1] * 11

cnt = dict()
for i in range(n):
    sz.append(len(str(a[i])))
    tmp = (sz[i], a[i] % k)
    if tmp in cnt:
        cnt[tmp] += 1
    else:
        cnt[tmp] = 1

t[0] = 1
for i in range(1, 11):
    t[i] = (t[i - 1] * 10) % k

ans = 0
for i in range(n):
    for l in range(1, 11):
        cur = (k - a[i] * t[l]) % k
        tmp = (l, cur)
        if tmp in cnt:
            ans += cnt[tmp]
        if (sz[i] == l and cur == a[i] % k):
            ans -= 1
print(ans)
