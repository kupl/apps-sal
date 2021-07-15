n,m = map(int,input().split())
swithes = [list(map(int,input().split())) for i in range(m)]
p = list(map(int,input().split()))
total = 0

for i in range(2**n):
    bag = []
    ans = 0
    for j in range(n):
        if i >> j & 1:
            bag.append(j+1)
    for k in range(m):
        a = 0
        for l in range(swithes[k][0]):
            if swithes[k][l+1] in bag:
                a += 1
        if a % 2 == p[k]:
            ans += 1
    
    if ans == m:
        total += 1

print(total)
