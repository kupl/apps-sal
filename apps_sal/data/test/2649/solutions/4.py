n = int(input())

x, y = [], []
for i in range(n):
    xi, yi = map(int, input().split())
    x.append(xi + yi)
    y.append(xi - yi)

x.sort()
y.sort()

ans = max((x[-1] - x[0]), (y[-1] - y[0]))
print(ans)
