(n, m) = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()
h = 0
ans = 0
for i in range(n - 1):
    ans += a[i] - 1
    if a[i] > h:
        h += 1
if h < max(a):
    ans += h
else:
    ans += a[-1] - 1
print(ans)
