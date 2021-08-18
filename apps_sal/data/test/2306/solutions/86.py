N = int(input())
t = [0] + list(map(int, input().split()))
v = [0] + list(map(int, input().split()))
max_speed_from_left = [0] * (N + 1)
max_speed_from_right = [0] * (N + 1)

for i in range(1, N):
    start = max_speed_from_left[i - 1]
    max_speed_from_left[i] = min(start + t[i], v[i], v[i + 1])

for i in range(N - 1, 0, -1):
    start = max_speed_from_right[i + 1]
    max_speed_from_right[i] = min(start + t[i + 1], v[i], v[i + 1])

speed = [min(x, y) for x, y in zip(max_speed_from_left, max_speed_from_right)]


def dist(left_speed, right_speed, t, v):
    x = (v - left_speed) + (v - right_speed)
    if x >= t:
        v = (left_speed + right_speed + t) / 2
        x = t
    d = (left_speed + v) * (v - left_speed) / 2
    d += v * (t - x)
    d += (right_speed + v) * (v - right_speed) / 2
    return d


ans = 0
for i in range(1, N + 1):
    ans += dist(speed[i - 1], speed[i], t[i], v[i])
print(ans)
