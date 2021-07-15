import math

N,X = list(map(int,input().split()))
x = list(map(int,input().split()))

arr = [0]*N
for i in range(N):
    arr[i] = abs(x[i]-X)
ans = arr[0]
for i in range(1,N):
    ans = math.gcd(ans, arr[i])
    
print(ans)
