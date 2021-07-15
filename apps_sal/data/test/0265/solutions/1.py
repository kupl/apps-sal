import sys

def popcount(i):
    assert 0 <= i < 0x100000000
    i = i - ((i >> 1) & 0x55555555)
    i = (i & 0x33333333) + ((i >> 2) & 0x33333333)
    return (((i + (i >> 4) & 0xF0F0F0F) * 0x1010101) & 0xffffffff) >> 24


N, M = list(map(int, sys.stdin.readline().split()))
table = [0]*(2**9)
for _ in range(N):
    S = tuple(map(int, sys.stdin.readline().split()))
    table[sum(2**(a-1) for a in S[1:])] += 1

dp = [0]*(2**9)
for s in range(2**9):
    ppc = popcount(s)
    res = table[s]
    t = s&(s-1)
    for _ in range(2**ppc - 1):
        res += table[t]
        t = (t-1)&s
    dp[s] = res                        

table = [False]*(2**9)
cost = [[] for _ in range(2**9)]
idx = [[] for _ in range(2**9)]
for i in range(M):
    T = tuple(map(int, sys.stdin.readline().split()))
    x = sum(2**(a-1) for a in T[2:])
    table[x] = True
    cost[x].append(T[0])
    idx[x].append(i+1)

minidx = [cost[x].index(min(cost[x])) if cost[x] else -1 for x in range(2**9)]
mincost = [10**10]*(2**9)
mincostidx = [(0, 0) for _ in range(2**9)]
reachable = [False]*(2**9)
for i in range(2**9):
    if not table[i]:
        continue
    for j in range(2**9):
        if not table[j]:
            continue
        reachable[i|j] = True
        if i != j:
            mi = min(cost[i])
            mj = min(cost[j])
            if mincost[i|j] > mi + mj:
                mincost[i|j] = mi + mj
                mincostidx[i|j] = (idx[i][minidx[i]], idx[j][minidx[j]])
ctr = -1
candi = []
for i in range(2**9):
    if not reachable[i]:
        continue
    if ctr > dp[i]:
        continue
    elif ctr == dp[i]:
        candi.append(i)
    else:
        ctr = dp[i]
        candi = [i]

ans = 10**11
Ans = (-1, -1)
for c in candi:
    if table[c] and len(cost[c]) > 1:
        D = cost[c][:]
        res = min(D)
        a = D.index(res)
        D.remove(res)
        r = min(D)
        b = D.index(r)
        if cost[c][b] != r:
            b += 1
        if a == b:
            b += 1
        res += r
        if ans > res:
            ans = res
            Ans = (idx[c][a], idx[c][b])
    if ans > mincost[c]:
        ans = mincost[c]
        Ans = mincostidx[c]
print(*Ans)

