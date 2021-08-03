N, M = list(map(int, input().split()))
a = list([int(x) - 1 for x in input().split()])
P = 300005
d1 = [0] * P
d2 = [0] * P
s = 0
for i in range(N - 1):
    x = a[i]
    y = a[i + 1]
    if y < x:
        y += M
    s += y - x
    if x + 1 < y:
        d1[x + 2] += 1
        d1[y + 1] -= 1
        d2[y + 1] += y - x - 1
        d1[M + x + 2] += 1
        d1[M + y + 1] -= 1
        d2[M + y + 1] += y - x - 1

ans = float('inf')
for i in range(3 * M):
    if i > 0:
        d1[i] += d1[i - 1]
        d2[i] += d2[i - 1]
    d2[i] -= d1[i]
    ans = min(ans, s + d2[i])

print(ans)
