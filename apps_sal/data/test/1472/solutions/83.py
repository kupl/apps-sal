# ABC160
n, x, y = list(map(int, input().split()))
l = [0] * (n - 1)
for i in range(1, n):
    for j in range(i + 1, n + 1):
        l[min(j - i, abs(i - x) + abs(j - y) + 1) - 1] += 1

for k in range(n - 1):
    print((l[k]))
