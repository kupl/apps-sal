import sys
input = lambda: sys.stdin.readline().rstrip()
N = int(input())
C = [int(a) - 1 for a in input().split()]
X = [[] for i in range(N)]
for i in range(N-1):
    x, y = map(int, input().split())
    X[x-1].append(y-1)
    X[y-1].append(x-1)

def EulerTour(n, X, i0):
    f = lambda k: k * (k + 1) // 2
    USED = [0] * n
    ORG = [0] * n
    TMP = [0] * n
    P = [-1] * n
    ct = -1
    ET1 = [0] * n
    ET2 = [0] * n
    ANS = [f(n)] * n
    IND = [0] * n
    i = i0
    while i >= 0:
        ind = IND[i]
        if ind == 0:
            if i: ORG[i] = USED[C[P[i]]]
            ct += 1
            ET1[i] = ct
        
        if ind >= len(X[i]):
            ET2[i] = ct
            USED[C[i]] += 1 + TMP[i]
            if i:
                k = ET2[i] - ET1[i] + 1 - USED[C[P[i]]] + ORG[i]
                ANS[C[P[i]]] -= f(k)
                TMP[P[i]] += k
            i = P[i]
            continue
        
        j = X[i][ind]
        if P[i] == j:
            IND[i] += 1
            continue
        P[j] = i
        IND[i] += 1
        i = j
    
    for i in range(n):
        ANS[i] -= f(n - USED[i])
    return ANS

print(*EulerTour(N, X, 0), sep = "\n")
