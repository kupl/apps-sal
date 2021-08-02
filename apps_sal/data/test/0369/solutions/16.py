import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))
S = list(input().rstrip())


def cost(S):
    minCost = [-1] * (N + 1)
    minCost[0] = 0
    ind = 1
    for i, s in enumerate(S):
        if s == "1":
            continue
        while i < ind <= min(i + M, N):
            if S[ind] == "0":
                minCost[ind] = minCost[i] + 1
            ind += 1
    return minCost


M1 = cost(S)
M2 = cost(S[::-1])[::-1]
if M1[-1] == -1:
    print((-1))
else:
    C = M1[-1]
    Inds = [10**14] * (C + 1)
    for i, (m1, m2) in enumerate(zip(M1, M2)):
        if m1 + m2 == C:
            Inds[m1] = min(Inds[m1], i)
    ans = []
    for i1, i2 in zip(Inds, Inds[1:]):
        ans.append(i2 - i1)
    print((*ans))
