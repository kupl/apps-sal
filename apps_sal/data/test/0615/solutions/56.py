n = int(input())
a = list(map(int, input().split()))
left = []
now = a[0]
le = 1
s = a[0]
for i in range(1, n):
    s += a[i]
    while le < i and abs(2 * now - s) > abs(2 * now + 2 * a[le] - s):
        now += a[le]
        le += 1
    left.append([now, s - now])
right = []
now = a[-1]
ri = 2
s = a[-1]
for i in range(2, n + 1):
    s += a[-i]
    while ri < i and abs(2 * now - s) > abs(2 * now + 2 * a[-ri] - s):
        now += a[-ri]
        ri += 1
    right.append([now, s - now])
ans = float('INF')
for i in range(n - 3):
    (a, b) = left[i]
    (c, d) = right[n - 4 - i]
    ans = min(ans, max(a, b, c, d) - min(a, b, c, d))
print(ans)
