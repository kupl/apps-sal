import math
n=int(input())
a=list(map(int,input().split()))

l="".join(["o" if i+1==a[i] else "x" for i in range(n)])
sl=l.split("x")
ss=[len(x) for x in sl]
ans=[math.ceil(i/2) for i in ss]
print(sum(ans))
