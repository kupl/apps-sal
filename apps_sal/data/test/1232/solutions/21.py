a,b = input().split()
a=int(a)
b=int(b)
k,m=input().split()
m=int(m)
k=int(k)
A=input().split()
B=input().split()
for i in range(a):
    A[i]=int(A[i])
for i in range(b):
    B[i]=int(B[i])

if(k<=a and A[k-1]<B[-m]):
    print("YES")
else:
    print("NO")

