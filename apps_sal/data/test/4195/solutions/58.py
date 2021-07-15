D,N=map(int,input().split())
a=100**(D)
A=[]
for i in range(1,101):
    A.append(i*a)
if D==0:
    A.remove(100)
    A.append(101)
elif D==1:
    A.remove(10000)
    A.append(10100)
elif D==2:
    A.remove(1000000)
    A.append(1010000)
print(A[N-1])
