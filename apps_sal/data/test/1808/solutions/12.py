y=input().split()
n = int(y[0])
k=int(y[1])
x=int(y[2])
a=[]
s=0
a=input().split()
for i in range(len(a)-k):
    s+=int(a[i])
s+=k*x
print(s)


