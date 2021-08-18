n, m = list(map(int, input().strip().split()))
color = list(map(int, input().strip().split()))

g = [[] for i in range(n)]

colors = {i: set() for i in sorted(color)}

for i in range(m):
    x, y = list(map(int, input().strip().split()))
    x -= 1
    y -= 1
    if color[x] != color[y]:
        colors[color[x]].add(color[y])
        colors[color[y]].add(color[x])
print(max(colors, key=lambda _: len(colors[_])))
