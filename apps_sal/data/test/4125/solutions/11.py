import math
N,X = map(int,input().split())
x = list(map(int,input().split()))
y = [abs(x[i]-X) for i in range(N)]
if N == 1:
    print(y[0])
    return
ans = math.gcd(y[0],y[1])
for i in range(2,N):
    ans = min(ans,math.gcd(y[i],ans))
print(ans)
