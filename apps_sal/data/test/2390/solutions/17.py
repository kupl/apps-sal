from itertools import accumulate
(N, C) = map(int, input().split())
XV = [tuple(map(int, input().split())) for _ in range(N)]
eat = 0
walk = 0
now = 0
clockwise = [(0, 0)]
for (x, v) in XV:
    eat += v
    walk += x - now
    clockwise.append((eat, walk))
    now = x
eat = 0
walk = 0
now = C
counter_clockwise = [(0, 0)]
for (x, v) in XV[::-1]:
    eat += v
    walk += now - x
    counter_clockwise.append((eat, walk))
    now = x
best_left_go = [e - w for (e, w) in counter_clockwise]
best_left_go = list(accumulate(best_left_go, func=max))
best_left_back = [e - 2 * w for (e, w) in counter_clockwise]
best_left_back = list(accumulate(best_left_back, func=max))
best_right_go = [e - w for (e, w) in clockwise]
best_right_go = list(accumulate(best_right_go, func=max))
best_right_back = [e - 2 * w for (e, w) in clockwise]
best_right_back = list(accumulate(best_right_back, func=max))
ans = 0
for (i, rb) in enumerate(best_right_back):
    calorie = rb + best_left_go[N - i]
    ans = max(ans, calorie)
for (i, lb) in enumerate(best_left_back):
    calorie = lb + best_right_go[N - i]
    ans = max(ans, calorie)
print(ans)
