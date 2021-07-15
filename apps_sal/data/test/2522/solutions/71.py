from itertools import accumulate
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def solve():
    INF = 10**10

    N = int(input())
    As = list(map(int, input().split())) + [INF]
    Bs = list(map(int, input().split())) + [INF]

    def f(As):
        sts = [-1] * (N+1)
        ens = [-1] * (N+1)
        i = 0
        for v in range(1, N+1):
            if As[i] == v:
                sts[v] = i
            else:
                continue
            while As[i] == v:
                i += 1
            ens[v] = i-1
        return (sts, ens)

    stAs, enAs = f(As)
    stBs, enBs = f(Bs)

    imoss = [0] * (2*N+1)
    for v in range(1, N+1):
        if stAs[v] == -1 or stBs[v] == -1: continue
        L = stAs[v] - enBs[v] + N
        R = enAs[v] - stBs[v] + N
        imoss[L] += 1
        imoss[R+1] -= 1

    imoss = list(accumulate(imoss))

    Cs = [imoss[i] + imoss[i+N] for i in range(N)]

    numShift = -1
    for i in range(N):
        if Cs[i] == 0:
            numShift = i
            break

    if numShift == -1:
        print('No')
    else:
        print('Yes')
        anss = [Bs[(i-numShift)%N] for i in range(N)]
        print((' '.join(map(str, anss))))


solve()

