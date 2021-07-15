import math
def lcm(x, y):
    return (x * y) // math.gcd(x, y)

n=int(input())
t=[]
for i in range(n):
    t.append(int(input()))

ans=t[0]
for i in range(1,n):
    ans=lcm(ans,t[i])
print(ans)

