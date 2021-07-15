N = int(input())
T = [int(a) for a in input().split()]
P = [-1] + [int(a)-1 for a in input().split()]
C = [[] for i in range(N)]
for i in range(1, N):
    C[P[i]].append(i)
L = sum([1 for i in range(N) if len(C[i]) == 0])
CT = [0] * N
DP = [-1] * N

i = 0
while i >= 0:
    # print("Try", i, C[i], CT[i])
    if CT[i] >= len(C[i]):
        if len(C[i]) == 0:
            DP[i] = 1
        elif T[i]:
            mi = 10**10
            for j in C[i]:
                mi = min(mi, DP[j])
            DP[i] = mi
        else:
            s = 0
            for j in C[i]:
                s += DP[j]
            DP[i] = s
        i = P[i]
    else:
        CT[i], i = CT[i] + 1, C[i][CT[i]]

print(L-DP[0]+1)

