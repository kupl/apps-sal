import sys

readline = sys.stdin.readline
readall = sys.stdin.read
ns = lambda: readline().rstrip()
ni = lambda: int(readline().rstrip())
nm = lambda: map(int, readline().split())
nl = lambda: list(map(int, readline().split()))
prn = lambda x: print(*x, sep='\n')

def solve():
    n, k = nm()
    p = nl()
    _c = nl()
    c = [0]*n
    for i in range(n):
        p[i] -= 1
        c[i] = _c[p[i]]
    m = 31
    MIN = - (1 << 63)
    vertex = list()
    score = list()
    vertex.append(p)
    score.append(c)
    for a in range(1, m+1):
        p_ath = [0] * n
        c_ath = [0] * n
        for i in range(n):
            p_ath[i] = vertex[a-1][vertex[a-1][i]]
            c_ath[i] = score[a-1][i] + score[a-1][vertex[a-1][i]]
        vertex.append(p_ath)
        score.append(c_ath)
    
    prv = [[MIN, 0] for _ in range(n)]
    nxt = [[MIN, MIN] for _ in range(n)] 
    for b in range(m, -1, -1):
        for i in range(n):
            if (k >> b) & 1:
                nxt[vertex[b][i]][0] = max(nxt[vertex[b][i]][0], prv[i][0] + score[b][i])
                nxt[vertex[b][i]][1] = max(nxt[vertex[b][i]][1], prv[i][1] + score[b][i])
                nxt[i][0] = max(nxt[i][0], prv[i][0], prv[i][1])
            else:
                nxt[vertex[b][i]][0] = max(nxt[vertex[b][i]][0], prv[i][0] + score[b][i])
                nxt[i][0] = max(nxt[i][0], prv[i][0])
                nxt[i][1] = max(nxt[i][1], prv[i][1])
        prv, nxt = nxt, prv
    ans = max(max(x) for x in prv)
    if ans == 0:
        ans = max(c)
    print(ans)    
    return

solve()
