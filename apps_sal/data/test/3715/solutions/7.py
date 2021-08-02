n = int(input())
a = list(map(int, input().split()))

d = [[10 ** 6] * 3 for i in range(n)]
d[0][0] = 1
if a[0] & 1:
    d[0][1] = 0
if a[0] & 2:
    d[0][2] = 0

for i in range(1, n):
    d[i][0] = min(d[i - 1]) + 1
    if a[i] & 1:
        d[i][1] = min(d[i - 1][0], d[i - 1][2])
    if a[i] & 2:
        d[i][2] = min(d[i - 1][0], d[i - 1][1])

print(min(d[-1]))
