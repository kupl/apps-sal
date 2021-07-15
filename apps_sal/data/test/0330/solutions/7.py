p,y = list(map(int,input().split()))
primes = []
m = int(min(y**0.5,p))
for i in range(2,m+1):
    pri = True
    for pp in primes:
        if i//pp*pp==i: 
            pri = False
            break
    if pri: primes.append(i)

sol = False
for yy in range(y,p,-1):
    ok = True
    for pp in primes:
        if yy//pp*pp==yy:
            ok = False
            break
    if ok:
        sol = yy
        break

if sol:
    print(sol)
else:
    print(-1)

