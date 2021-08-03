import sys
readline = sys.stdin.readline

inf = 10**16


def calc(m, L, R):
    N = len(L)
    cl = 0
    cr = 0
    ss = 0
    candi = []
    for i in range(N):
        if L[i] > m:
            cr += 1
            ss += L[i]
        elif R[i] < m:
            cl += 1
            ss += L[i]
        else:
            candi.append(L[i])
    cm = len(candi)
    if cl > N // 2:
        return inf
    k = min(cm, N // 2 - cl)
    candi.sort()
    ss += sum(candi[:k])
    ss += (cm - k) * m

    return ss


T = int(readline())
Ans = [None] * T
for qu in range(T):
    M, LS = list(map(int, readline().split()))
    L = [None] * M
    R = [None] * M
    for i in range(M):
        L[i], R[i] = list(map(int, readline().split()))

    ok = 0
    ng = 10**9 + 1
    while abs(ok - ng) > 1:
        med = (ok + ng) // 2
        if calc(med, L, R) <= LS:
            ok = med
        else:
            ng = med
    Ans[qu] = ok

print('\n'.join(map(str, Ans)))
