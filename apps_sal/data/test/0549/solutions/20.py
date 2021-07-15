n=int(input())
b=int(n**0.5)
f=True
for i in range(b,1,-1):
    if n%i==0:
        print(min(n//i,i),max(n//i,i))
        f=False
        break
if f:
    print(1,n)

