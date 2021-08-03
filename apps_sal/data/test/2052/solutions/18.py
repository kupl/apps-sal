w, l = list(map(int, input().split()))
a = list(map(int, input().split()))
for i in range(1, w - 1):
    a[i] = a[i] + a[i - 1]
ans = a[l - 1]
for i in range(l, w - 1):
    ans = min(ans, a[i] - a[i - l])
print(ans)
