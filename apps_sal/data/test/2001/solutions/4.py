n,q = list(map(int, input().split()))
a = input()
Q = []
for _ in range(q):
    Q.append(list(map(int, input().split())))
d = [0]
ab = 0
for i in a:
    if i == '1':
        ab += 1
    d.append(ab)
mod = int(1e9 + 7)
p = [1]
i = 1
for _ in range(n):
    i = (i*2)%mod
    p.append(i)
    
for l,r in Q:
    y = r-l + 1
    x = d[r] - d[l-1]
    y -= x
    print(((p[x]-1)*p[y])%mod)
