n, x, y = list(map(int, input().split()))
ans = [0 for _ in range(n)]

for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        a = min(abs(i - j), abs(x - i) + +abs(j - y) + 1, abs(y - i) + abs(j - x) + 1)
        ans[a] += 1
for i in range(1, n):
    print((ans[i]))
