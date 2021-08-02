import bisect
n, d, a = map(int, input().split())
fox = [None] * n
for i in range(n):
    x, h = map(int, input().split())
    fox[i] = (x, h)

fox.sort()
x = [int(fox[i][0]) for i in range(n)]
h = [int(fox[i][1]) for i in range(n)]

ans = 0
bit = [0] * n
for i in range(n):
    if i != 0:
        bit[i] += bit[i - 1]
    if bit[i] >= h[i]:
        continue
    sub = (h[i] - bit[i] - 1) // a + 1
    ans += sub
    bit[i] += sub * a
    index = bisect.bisect_right(x, x[i] + 2 * d)
    if index == n:
        continue
    bit[index] -= sub * a
print(ans)
