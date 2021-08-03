N = int(input())
T = list(map(int, input().split()))
V = list(map(int, input().split()))


MAX_V = [0]
for t, v in zip(T, V):
    MAX_V[-1] = min(MAX_V[-1], v)
    for ti in range(t * 2):
        MAX_V.append(v)


N = len(MAX_V)
Feasible_V = [0] * N
for i in range(N - 1):
    Feasible_V[i + 1] = min(Feasible_V[i] + 0.5, MAX_V[i + 1])

Feasible_V[-1] = 0
for i in reversed(list(range(1, N))):
    Feasible_V[i - 1] = min(Feasible_V[i - 1], Feasible_V[i] + 0.5)


ans = 0
for i in range(N - 1):
    x1, x2 = Feasible_V[i], Feasible_V[i + 1]
    ans += (x1 + x2) * 0.5 / 2

print(ans)
