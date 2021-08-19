N = int(input())
T = [int(i) for i in input().split()]
V = [int(i) for i in input().split()]
Ts = sum(T)
Vmax = [float('inf')] * (Ts * 2 + 1)
ts = 0
for i in range(N):
    for t in range(T[i]):
        t1 = (ts + t) * 2
        t2 = (ts + t) * 2 + 1
        Vmax[t1] = min(Vmax[t1], V[i])
        Vmax[t2] = min(Vmax[t2], V[i])
    Vmax[(ts + T[i]) * 2] = min(Vmax[(ts + T[i]) * 2], V[i])
    ts += T[i]
Vmax[0] = Vmax[Ts * 2] = 0
for t in range(Ts * 2):
    Vmax[t + 1] = min(Vmax[t + 1], Vmax[t] + 0.5)
for t in range(Ts * 2 - 1, 0, -1):
    Vmax[t] = min(Vmax[t], Vmax[t + 1] + 0.5)
ans = 0.0
for i in range(Ts * 2):
    ans += (Vmax[i] + Vmax[i + 1]) * 0.5 / 2
print(ans)
