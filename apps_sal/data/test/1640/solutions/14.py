n = int(input())
cnt = dict()
s = 0
ans = 0
a = list(map(int, input().split()))
for i in range(0, n):
    ans += a[i] * i - s
    ans -= cnt.get(a[i] - 1, 0)
    ans += cnt.get(a[i] + 1, 0)
    s += a[i]
    cnt[a[i]] = cnt.get(a[i], 0) + 1
print(ans)
