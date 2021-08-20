N = int(input())
T = list([int(t) * 10 for t in input().split()])
V = list(map(int, input().split())) + [0]
R = sum(T)
maxSpeed = [10 ** 18] * (R + 1)
maxSpeed[0] = 0
maxSpeed[R] = 0
now = 0
for (i, t) in enumerate(T):
    now += t
    maxSpeed[now] = min(V[i], V[i + 1])
now = 0
for (v, t) in zip(V, T):
    for i in range(t + 1):
        maxSpeed[now + i] = min(maxSpeed[now + i], v)
    now += t
for t in range(1, R + 1):
    maxSpeed[t] = min(maxSpeed[t], maxSpeed[t - 1] + 0.1)
for t in range(R)[::-1]:
    maxSpeed[t] = min(maxSpeed[t], maxSpeed[t + 1] + 0.1)
base = 0
upper = 0
for (v1, v2) in zip(maxSpeed, maxSpeed[1:]):
    base += min(v1, v2)
    upper += abs(v1 - v2)
ans = base + upper / 2
print(ans / 10)
