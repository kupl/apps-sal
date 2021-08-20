(n, l) = list(map(int, input().split()))
a = list(map(int, input().split()))
a = sorted(a)
ans = float(0.0)
for i in range(len(a) - 1):
    ans = max(ans, (a[i + 1] - a[i]) / 2)
ans = max(a[0], ans)
ans = max(l - a[len(a) - 1], ans)
print(ans)
