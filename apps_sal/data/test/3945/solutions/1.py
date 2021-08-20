import sys
input = sys.stdin.readline
(n, m) = list(map(int, input().split()))
St = [list(map(int, input().split())) for _ in range(n)]
ppr = [sorted(list(set(s))) for s in St]
PR = []
for i in range(n):
    H = dict()
    for (j, v) in enumerate(ppr[i], 1):
        H[v] = j
    PR.append([H[p] for p in St[i]] + [j])
TSt = list(map(list, list(zip(*St))))
ppc = [sorted(list(set(s))) for s in TSt]
PC = []
for i in range(m):
    H = dict()
    for (j, v) in enumerate(ppc[i], 1):
        H[v] = j
    PC.append([H[p] for p in TSt[i]] + [j])
for i in range(n):
    pri = PR[i]
    prm = PR[i][-1]
    print(*[max(pri[j], PC[j][i]) + max(prm - pri[j], PC[j][-1] - PC[j][i]) for j in range(m)])
