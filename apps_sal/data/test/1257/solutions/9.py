(n, k) = map(int, input().split())
a = n * (k - 1) + 1
sm = n * (2 * a + (n - 1) * (n - k + 1)) // 2
t = [[0] * n for i in range(n)]
x = 1
for j in range(k - 1):
    for i in range(n):
        t[i][j] = x
        x += 1
for i in range(n):
    for j in range(k - 1, n):
        t[i][j] = x
        x += 1
print(sm)
for row in t:
    print(' '.join(map(str, row)))
