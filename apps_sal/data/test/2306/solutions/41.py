N = int(input())
T = [0] + list(map(int, input().split()))
V = [-1] + list(map(int, input().split()))

ans = 0
for i in range(1, N + 1):
    T[i] += T[i - 1]
time = T[-1]
upper = {}

state = N
speed = 0

for t in range(2 * time, 0, -1):
    t *= 0.5
    if T[state - 1] == t:
        speed = min(V[state], speed)
        state -= 1
    upper[t] = min(speed, V[state])
    speed += 0.5

speed = 0
pre = -1
Ans = []
for t in range(1, 2 * time + 1):
    t = t * 0.5
    speed += 0.5
    speed = min(speed, upper[t])
    Ans.append(speed)
    if pre == speed:
        ans += 0.5 * speed
    elif pre > speed:
        ans += 0.5 * speed + 0.125
    else:
        ans += 0.5 * speed - 0.125
    pre = speed
print(ans)
