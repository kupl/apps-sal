n = int(input())
xs = []
ys = []
for i in range(n):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)
print(max(max(xs) - min(xs), max(ys) - min(ys)) ** 2)
