import sys
def input(): return sys.stdin.readline().rstrip()


N = int(input())
C = [int(a) - 1 for a in input().split()]
X = [[] for i in range(N)]
for i in range(N - 1):
    x, y = map(int, input().split())
    X[x - 1].append(y - 1)
    X[y - 1].append(x - 1)


def EulerTour(n, X, i0):
    def f(k): return k * (k + 1) // 2
    USED = [0] * n
    ORG = [0] * n
    TMP = [0] * n
    P = [-1] * n
    Q = [~i0, i0]
    ct = -1
    ET1 = [0] * n
    ET2 = [0] * n
    ANS = [f(n)] * n
    done = [0] * n
    while Q:
        i = Q.pop()
        if i < 0:
            i = ~i
            ET2[i] = ct
            USED[C[i]] += 1 + TMP[i]
            if i:
                k = ET2[i] - ET1[i] + 1 - USED[C[P[i]]] + ORG[i]
                ANS[C[P[i]]] -= f(k)
                TMP[P[i]] += k
            continue
        done[i] = 1
        if i:
            ORG[i] = USED[C[P[i]]]
        ct += 1
        ET1[i] = ct
        for a in X[i]:
            if done[a]:
                continue
            P[a] = i
            Q.append(~a)
            Q.append(a)
    for i in range(n):
        ANS[i] -= f(n - USED[i])
    return ANS


print(*EulerTour(N, X, 0), sep="\n")
