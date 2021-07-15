import math
N, X = [int(i) for i in input().split()]
x = [int(i) for i in input().split()]
x.append(X)
x.sort()

xdst = [x[i+1] - x[i] for i in range(N)]
#print(xdst)

ans = 10**10
if len(xdst) == 1:
    print(xdst[0])
    return

for i in range(N-1):
    ans = min(math.gcd(xdst[i], xdst[i+1]),ans)
print(ans)
