n = int(input())
T = [0] + list(map(int, input().split()))
V = [0] + list(map(int, input().split())) + [0]

unit = 2

acumT = [0] * (n + 1)
for i in range(n):
    acumT[i + 1] = acumT[i] + T[i + 1]

PV = [0] * (sum(T) * unit + 1)
for p in range(1, n + 1):
    t1 = acumT[p - 1]
    t2 = acumT[p]
# for (t1, t2), (v1, v2, v3) in zip(zip(acumT, acumT[1:]), zip(V, V[1:], V[2:])):
    for i in range(t1 * unit, t2 * unit + 1):
        ii = i / unit
        PV[i] = min([ii - acumT[k] + V[k] for k in range(0, p)] + [V[p]] + [-ii + acumT[m] + V[m + 1] for m in range(p, n + 1)])

area = sum((i + j) / unit / 2 for i, j in zip(PV, PV[1:]))
print(area)
