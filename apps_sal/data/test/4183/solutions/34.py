def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

def lcm(a,b):
    return a*b//gcd(a,b)
      
N=int(input())
T=[]
total=1
for i in range(N):
    a=int(input())
    T.append(a)
T_set=sorted(list(set(T)))
M=len(T_set)

ans=T_set[0]
if M==1:
    ans=T_set[0]
else:
    for i in range(1,M):
        ans=lcm(ans,T_set[i])

print(ans)
