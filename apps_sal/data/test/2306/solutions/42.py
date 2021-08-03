n = int(input())
t = list(map(int, input().split()))
u = list(map(int, input().split()))
speed = [0]
for i in range(n):
    speed += [u[i]] * t[i] * 2
speed.append(0)
m = len(speed)
for i in range(1, m):
    speed[i - 1] = min(speed[i - 1], speed[i])
del speed[-1]
m -= 1
for i in range(1, m):
    speed[i] = min(speed[i], speed[i - 1] + 0.5)
for i in range(m - 2, -1, -1):
    speed[i] = min(speed[i], speed[i + 1] + 0.5)
ans = 0
for i in range(1, m):
    ans += abs(speed[i - 1] + speed[i]) * 0.25
print(ans)
