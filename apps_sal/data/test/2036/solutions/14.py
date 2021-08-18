import sys
input = sys.stdin.readline

n, m, x, y = map(int, input().split())
x -= 1
y -= 1
ans = []
for _ in range(n):
    for j in range(m):
        ans.append((x + 1, y + 1))
        if j != m - 1:
            y = (y + 1) % m
        else:
            x = (x + 1) % n

for x, y in ans:
    print(x, y)
