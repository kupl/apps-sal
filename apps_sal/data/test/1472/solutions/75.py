(n, x, y) = map(int, input().split())
(x, y) = (x - 1, y - 1)
d = [0 for i in range(n)]
for i in range(n):
    for j in range(i + 1, n):
        m = min(abs(i - j), abs(x - i) + abs(y - j) + 1, abs(x - j) + abs(y - i) + 1)
        d[m] += 1
for i in range(n - 1):
    print(d[i + 1])
