(n, h) = list(map(int, input().split()))
a = [0] * n
b = [0] * n
for i in range(n):
    (a[i], b[i]) = list(map(int, input().split()))
a = sorted(a, reverse=True)
b = sorted(b, reverse=True)
ans = 0
i = 0
while i < n and a[0] < b[i]:
    h -= b[i]
    i += 1
    ans += 1
    if h <= 0:
        break
if h <= 0:
    print(ans)
else:
    print(ans + (h + a[0] - 1) // a[0])
