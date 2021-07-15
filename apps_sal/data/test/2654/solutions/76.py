n=int(input())
m=[]
M=[]
for _ in range(n):
    x,y=map(int,input().split())
    m.append(x)
    M.append(y)
m=sorted(m)
M=sorted(M)

z=n//2
if n%2==1:
    a=m[z]
    b=M[z]
    print(b-a+1)
else:
    a=m[z]+m[z-1]
    b=M[z]+M[z-1]
    print(b-a+1)
