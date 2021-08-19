import sys


def input():
    return sys.stdin.readline().rstrip()


N = int(input())
C = [int(a) - 1 for a in input().split()]
X = [[] for i in range(N)]
head = [-1] * (N + 1)
to = [0] * (N - 1 << 1)
nxt = [0] * (N - 1 << 1)
for i in range(N - 1):
    (x, y) = map(int, input().split())
    (x, y) = (x - 1, y - 1)
    nxt[i] = head[x]
    to[i] = y
    head[x] = i
    j = i + N - 1
    nxt[j] = head[y]
    to[j] = x
    head[y] = j


def EulerTour(n, i=0):

    def f(k):
        return k * (k + 1) // 2
    USED = [0] * n
    ORG = [0] * n
    TMP = [0] * n
    ANS = [f(n)] * n
    P = [-1] * n
    ct = 0
    ET1 = [0] * n
    ET2 = [0] * n
    while i >= 0:
        e = head[i]
        if e < 0:
            ET2[i] = ct
            USED[C[i]] += 1 + TMP[i]
            if i:
                k = ET2[i] - ET1[i] + 1 - USED[C[P[i]]] + ORG[i]
                ANS[C[P[i]]] -= f(k)
                TMP[P[i]] += k
            i = P[i]
            continue
        j = to[e]
        if P[i] == j:
            head[i] = nxt[e]
            continue
        P[j] = i
        head[i] = nxt[e]
        i = j
        ORG[i] = USED[C[P[i]]]
        ct += 1
        ET1[i] = ct
    for i in range(n):
        ANS[i] -= f(n - USED[i])
    return ANS


print(*EulerTour(N, 0), sep='\n')
