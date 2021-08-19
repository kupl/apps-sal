n = int(input())
max_x = 0
max_y = 0
max_s = 0
for _ in range(n):
    (x, y) = map(int, input().split())
    if x + y > max_s:
        max_s = x + y
        max_x = x
        max_y = y
print(max_s)
