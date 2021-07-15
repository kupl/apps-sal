import math
def lcm(x,y):
    return (x*y)//(math.gcd(x,y))

n=int(input())
t=[int(input()) for _ in range(n)]
ans=1
for i in t:
    ans=lcm(i,ans)
print(ans)
