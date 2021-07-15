import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = list(map(int, input().split()))
    graph[a-1].append(b-1)

L = 10**14
num = -1
for n in range(N):
    q = [n]
    checked = [False]*N
    checked[n] = True
    before = [None]*N
    c = 0
    ok = False
    while q:
        c += 1
        qq = []
        for p in q:
            for np in graph[p]:
                if not checked[np]:
                    before[np] = p
                    qq.append(np)
                    checked[np] = True
                elif np == n:
                    before[np] = p
                    ok = True
                    break
        if ok: break
        q = qq
    
    if ok and c < L:
        L = c
        num = n
        ans = []
        k = n
        for _ in range(c):
            k = before[k]
            ans.append(k+1)

if num == -1:
    print((-1))
else:
    print((len(ans)))
    for a in reversed(ans):
        print(a)    

