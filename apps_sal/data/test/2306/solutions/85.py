N = int(input())
t = list(map(int, input().split()))
v = list(map(int, input().split()))


V = [100] * (2 * sum(t) + 1)
T = 0
for i in range(N):
    for j in range(T + 1, T + t[i] * 2 + 1):
        V[j] = min(V[j], v[i])
    T += t[i] * 2

for i in range(min(len(V), 201)):
    V[i] = min(V[i], i * 0.5)
for i in range(min(len(V), 201)):
    V[-i - 1] = min(V[-i - 1], i * 0.5)
V
T = 0
for i in range(N - 1):
    T += t[i] * 2
    vi = min(V[T], v[i], v[i + 1])
    for j in range(201):
        if T - j >= 0:
            V[T - j] = min(V[T - j], vi + 0.5 * j)
        if T + j <= len(V) - 1:
            V[T + j] = min(V[T + j], vi + 0.5 * j)

V
ans = 0
for i in range(len(V) - 1):
    ans += 0.5 * 0.5 * (V[i] + V[i + 1])
print(ans)
