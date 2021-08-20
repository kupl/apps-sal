from itertools import accumulate
n = int(input())
a = list(map(int, input().split()))
c = list(accumulate(a))
ans = float('inf')
(x, y) = (0, 2)
for i in range(1, n - 2):
    while c[x] < c[i] - c[x + 1]:
        x += 1
    y = max(y, i + 1)
    while c[y] - c[i] < c[-1] - c[y + 1]:
        y += 1
    ma = max(c[x], c[i] - c[x], c[y] - c[i], c[-1] - c[y])
    mi = min(c[x], c[i] - c[x], c[y] - c[i], c[-1] - c[y])
    ans = min(ans, ma - mi)
print(ans)
