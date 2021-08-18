n, x, y = list(map(int, input().split()))

a = [0] * n


for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        s = min(j - i, abs(x - i) + abs(y - j) + 1)
        a[s - 1] += 1
        s = 10000000

for i in range(n - 1):
    print((a[i]))
