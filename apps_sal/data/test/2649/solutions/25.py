N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]
z = []
w = []
for (x, y) in XY:
    z.append(x + y)
    w.append(x - y)
print(max(max(z) - min(z), max(w) - min(w)))
