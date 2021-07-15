n, m = map(int, input().split())
maps = []
for i in range(n):
    maps.append(input())
up, down = 0, 0
for i in range(m):
    current = 0
    for j in range(n):
        if maps[j][i] == '*':
            current += 1
    if i:
        up = max(up, current - previous)
        down = max(down, previous - current)
    previous = current
print(up, down)
