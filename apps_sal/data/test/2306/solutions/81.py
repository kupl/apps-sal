N = int(input())
*T, = map(int, input().split())
*V, = map(int, input().split())
speed = [0]  # speed[i]: speed of train after 0.5*i seconds
for t, v in zip(T, V):
    speed[-1] = min(speed[-1], v)
    speed += [v] * (2 * t)
speed[-1] = 0
temp = 0
for t in range(1, len(speed)):
    speed[t] = temp = min(speed[t], temp + 0.5)
temp = 0
for t in range(len(speed) - 1, 0, -1):
    speed[t] = temp = min(speed[t], temp + 0.5)
ans = sum((v1 + v2) / 4 for v1, v2 in zip(speed, speed[1:]))
print(ans)
