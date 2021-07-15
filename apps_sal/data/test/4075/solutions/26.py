n, m = map(int, input().split())
ks = [list(map(int, input().split())) for i in range(m)]
p = list(map(int, input().split()))
ans = 0

for i in range(2**n):
    judge = True
    switch = [('off') for _ in range(n)]
    for j in range(len(switch)):
        if (i >> j) & 1:
            switch[j] = 'on'
    for k in range(m):
        count = 0
        for l in range(ks[k][0]):
            if switch[ks[k][l+1]-1] == 'on':
                count += 1
        if count % 2 != p[k]:
            judge = False
            break
    if judge == True:
        ans += 1

print(ans)
