n,m = list(map(int,input().split()))
ks = [list(map(int,input().split())) for i in range(m)]
p = list(map(int,input().split()))


ans = 0
for i in range(2**n):
    s = 0
    for j in range(m):
        c = 0
        for k in range(len(ks[j])-1) :
            if ((i >> (ks[j][k+1]-1)) & 1) :
                c += 1
        if c % 2 == p[j]:
            s += 1
    if s == m :
        ans += 1

print(ans)

