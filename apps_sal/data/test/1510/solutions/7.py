def R(): return map(int, input().split())


n, m = R()
a = sorted(R())
b = sorted(R())
b.reverse()
ans = 0
for i in range(min(n, m)):
    if b[i] > a[i]:
        ans += b[i] - a[i]
print(ans)
