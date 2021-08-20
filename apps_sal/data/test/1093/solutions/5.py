(h, w) = list(map(int, input().split()))
mountains = [input() for i in range(h)]
heights = [0 for i in range(w)]
for x in range(w):
    for y in range(h):
        if mountains[h - 1 - y][x] == '*':
            heights[x] = y
up = 0
down = 0
for i in range(w - 1):
    a = heights[i]
    b = heights[i + 1]
    c = abs(a - b)
    if a > b and c > down:
        down = c
    if a < b and c > up:
        up = c
print(up, down)
