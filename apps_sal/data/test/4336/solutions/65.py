W, H, x, y = map(int, input().split())
max_smaller = W * H / 2
way = 0
if x == W / 2 and y == H / 2:
    way = 1
print(max_smaller, way)
