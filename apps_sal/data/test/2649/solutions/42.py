n = int(input())
a, b = [], []
for _ in range(n):
    x, y = map(int, input().split())
    a.append(x + y)
    b.append(x - y)

a.sort()
b.sort()

ans = max(a[-1] - a[0], b[-1] - b[0])
print(ans)
