N = int(input())
T = [int(a) for a in input().split()]
P = [int(a)-1 for a in input().split()]
C = [[] for i in range(N)]
for i in range(N-1):
    C[P[i]].append(i+1)
L = [i for i in range(N) if len(C[i]) == 0]
DP = [-1] * N
def calc(i):
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

for i in range(N)[::-1]:
    calc(i)

print(len(L)-DP[0]+1)

