nk = list(map(int, input().split()))
n, k = nk[0], nk[1]
balls = {}
for ball in list(map(int, input().split())):
    if ball in balls:
        balls[ball] += 1
    else:
        balls[ball] = 1


size = len(list(balls.keys()))
swap_balls = list([(x[1], x[0]) for x in list(balls.items())])
swap_balls.sort()
count = 0

for ball_count, ball_number in swap_balls:
    if size <= k:
        break
    else:
        count += ball_count
        size -= 1

print(count)

