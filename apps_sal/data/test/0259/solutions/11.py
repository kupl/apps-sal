n,t=[int(i) for i in input().split()]
sd =[[int(i) for i in input().split()] for j in range(n)]

res = -1
best = 10**10

for i in range(n):
    s,d=sd[i]
    if t<=s:
        if s<best:
            best=s
            res=i
    else:
        left = t-s
        times = left//d
        if left%d!=0:
            times+=1
        s+=d*times
        if s<best:
            best=s
            res=i
print(res+1)

