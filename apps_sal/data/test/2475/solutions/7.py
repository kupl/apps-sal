n = int(input())
a = [int(i) for i in input().split()]
ans = 0
for C in range(1, n):
    f = 0
    for k in range([int(((n - 1) / C + 1) / 2), int((n - 1) / C)][(n - 1) % C != 0]):
        f += a[k * C] + a[n - 1 - k * C]
        ans = max(ans, f)
print(ans)
