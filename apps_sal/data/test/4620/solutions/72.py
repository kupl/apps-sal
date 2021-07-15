N = int(input())
csf = [list(map(int, input().split())) for _ in range(N-1)]
ans = [None]*N
ans[-1] = 0
for i in range(N-1):
    now = 0
    for j in range(i,N-1):
        if now <= csf[j][1]:
            now = csf[j][1]
        else:
            t  = (now - csf[j][1] + csf[j][2]-1)//csf[j][2]
            now = csf[j][1] + t*csf[j][2]
        now += csf[j][0]
    ans[i] = now
[print(a) for a in ans]
