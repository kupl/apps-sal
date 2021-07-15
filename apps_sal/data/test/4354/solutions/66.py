def LI():
    return list(map(int, input().split()))


def LIHW(h):
    return [list(map(int, input().split())) for _ in range(h)]


N, M = LI()
Nlist = LIHW(N)
Mlist = LIHW(M)
anslist = [0]*N
for i in range(N):
    a, b = Nlist[i]
    ans = 10**9
    for j in range(M):
        c, d = Mlist[j]
        kyori = abs(c-a)+abs(d-b)
        if ans > kyori:
            ansind = j+1
            ans = kyori
    anslist[i] = ansind

for i in range(N):
    print((anslist[i]))

