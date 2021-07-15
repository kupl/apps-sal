N = int(input())
T = [int(a) for a in input().split()]
P = [int(a)-1 for a in input().split()]
C = [[] for i in range(N)]
for i in range(N-1):
    C[P[i]].append(i+1)
L = sum([1 for i in range(N) if len(C[i]) == 0])
DP = [-1] * N
def calc(i):
    if len(C[i]) == 0:
        DP[i] = 1
    else:
        X = [DP[j] for j in C[i]]
        DP[i] = min(X) if T[i] else sum(X)

for i in range(N)[::-1]:
    calc(i)

print(L-DP[0]+1)

