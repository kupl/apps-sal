N = int(input())
t = list(map(int, input().split()))
v = list(map(int, input().split()))
T = sum(t) * 2
vt = [i / 2 if i < T / 2 else (T - i) / 2 for i in range(T + 1)]
ts = 0
te = 0
for (i, ti) in enumerate(t):
    te += ti * 2
    vi = v[i]
    for j in range(ts, te):
        vt[j] = min(vt[j], vi)
    for j in range(te, T):
        if vt[j] >= (j - te) / 2 + vi:
            vt[j] = (j - te) / 2 + vi
        else:
            break
    for j in range(ts - 1, -1, -1):
        if vt[j] >= -(j - ts) / 2 + vi:
            vt[j] = -(j - ts) / 2 + vi
        else:
            break
    ts = te
print(sum(vt) / 2)
