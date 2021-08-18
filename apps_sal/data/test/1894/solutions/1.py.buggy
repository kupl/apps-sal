n, m = [int(i) for i in input().split()]
current_floor = list(input())

x, t, direction = 0, 0, 1

for i in range(n - 1):
    floor = list(input())
    l, r = x, x
    wall = 0
    while True:
        t += 1
        if floor[x] == '.':
            break
        if (x + direction == m) or (x + direction < 0) or (current_floor[x + direction] == '#'):
            wall += 1
            direction = -direction
            if wall == 2:
                print("Never")
                return
        elif current_floor[x + direction] == '+':
            wall = 0
            current_floor[x + direction] = '.'
            direction = -direction
        elif l <= x + direction and x + direction <= r:
            if direction == 1:
                t += r - x - 1
                x = r
            else:
                t += x - l - 1
                x = l
        else:
            x += direction
            r = max(r, x)
            l = min(l, x)
    current_floor, floor = floor, current_floor
print(t)
