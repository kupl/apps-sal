N = int(input())
T = list(map(int, input().split()))
V1 = list(map(int, input().split()))
V1.append(0)

ST = [0] * (N + 1)
for i in range(N):
    ST[i + 1] = ST[i] + T[i]

V2 = [0] * N
for i in range(N):
    V2[i] = V1[i + 1] + ST[i + 1]
z = V2[-1]
for i in range(N - 1, -1, -1):
    if V2[i] > z:
        V2[i] = z
    else:
        z = V2[i]


Vmax = [0] * (ST[-1] * 2 + 1)
j = 0
t = 0
for i, Tn in enumerate(ST):
    while t < Tn or j == 0:
        Vmax[2 * t + j] = min(V1[i - 1], V2[i - 1])
        V2 = [x - 0.5 for x in V2]
        t += j
        j ^= 1

v, cnt = 0, 0
for i in range(ST[-1] * 2):
    nVmax = Vmax[i + 1]
    nv = min(v + 0.5, nVmax)
    cnt += (v + nv) * 0.5 / 2
    v = nv

print(cnt)
