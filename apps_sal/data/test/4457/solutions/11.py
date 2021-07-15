#Starting 8 minutes late !
def fun(x):
    return x[0]
n=int(input())
a=list(map(int,input().strip().split()))
for i in range(n):
    a[i]=[a[i],i+1]
a.sort(key=fun,reverse=True)
op=0
op2=""
for i in range(n):
    op2+=str(a[i][1])+" "
    op+=a[i][0]*i+1
print(op)
print(op2)
