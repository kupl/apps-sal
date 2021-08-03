n = int(input())
px, py = [], []
for i in range(n):
    x, y = list(map(int, input().split()))
    px.append(x)
    py.append(y)
print(max(max(px) - min(px), max(py) - min(py))**2)
