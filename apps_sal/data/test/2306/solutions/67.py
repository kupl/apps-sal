from itertools import accumulate
N = int(input())
T = [int(s) for s in input().split()]
V = [int(s) for s in input().split()] + [0]
lt = sum(T)
S = list(accumulate(T))
for i in range(len(T), 0, -1):
    V[i - 1] = min(V[i - 1], V[i] + T[i - 1])
vel2 = [0] * (2 * lt + 1)
for i in range(len(T)):
    ti = T[i]
    tr = S[i]
    for ts in range(tr - ti, tr):
        for t in (2 * ts + 1, 2 * ts + 2):
            if vel2[t - 1] - (2 * tr - (t - 1)) == 2 * V[i + 1]:
                vel2[t] = vel2[t - 1] - 1
            elif vel2[t - 1] == 2 * V[i]:
                vel2[t] = vel2[t - 1]
            else:
                vel2[t] = vel2[t - 1] + 1
ans = sum([(vel2[t - 1] + vel2[t]) / 8 for t in range(1, 2 * lt + 1)])
print(ans)
