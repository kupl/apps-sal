(n, x, y) = list(map(int, input().split()))
x = x - 1
y = y - 1
ans = [0] * (n - 1)
for i in range(n):
    for j in range(i + 1, n):
        shortest = min(abs(j - i), abs(x - i) + abs(y - j) + 1, abs(y - i) + abs(x - j) + 1)
        ans[shortest - 1] += 1
for a in ans:
    print(a)
