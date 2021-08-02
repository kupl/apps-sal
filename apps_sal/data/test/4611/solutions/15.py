n = int(input())

prev_t, prev_x, prev_y = 0, 0, 0
for _ in range(n):
    t, x, y = map(int, input().split())
    if (abs(x - prev_x) + abs(y - prev_y) <= t - prev_t
            and (abs(x - prev_x) + abs(y - prev_y)) % 2 == (t - prev_t) % 2):
        prev_t, prev_x, prev_y = t, x, y
        continue
    else:
        print('No')
        break
else:
    print('Yes')
