import math

n, I = map(int, input().split())
if I >= n*round(math.log(n,2)+0.5)/8:
    print(0)
else:
    a = sorted([x for x in map(int, input().split())])
    a=[-1]+a
    b=[i for i in range(n) if a[i] < a[i+1]]
    ans = set()
    for x in zip(b, b[2**(I*8//n):]+[n]):
        ans.add(x[1]-x[0])
    print(n-max(ans))
