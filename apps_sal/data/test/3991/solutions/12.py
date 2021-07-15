n=int(input())
V=list(map (int,input().split()))
V.sort()
Mod=int(1e9+7)
Sum=0
p=[1]
for i in range(n):
    p.append(p[i]*2%Mod)
for i in range(n-1):
    l=(p[i+1]+Mod-1)%Mod
    r=(p[n-i-1]-1+Mod)%Mod
    Sum=(Sum+(V[i+1]-V[i])*l*r)%Mod
print(int(Sum))

