n = int(input())
x = []
y = []
for i in range(n):
    p, q = list(map(int, input().split()))
    x.append(p)
    y.append(q)
dx = max(x) - min(x)
dy = max(y) - min(y)
print(max(dx, dy) ** 2)
