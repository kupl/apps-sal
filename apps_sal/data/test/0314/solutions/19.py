(n, k) = map(int, input().split())
a = list(map(int, input().split()))
s = 0
res = 0
ans = -1
for i in range(n):
    s += a[i]
    res += min(s, 8)
    s -= min(s, 8)
    if res >= k:
        ans = i + 1
        break
print(ans)
