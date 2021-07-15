n=int(input())
a=list(map(int,input().split()))
b=a+a
# print(b)
c=0
k=0
for i in range(2*n):
    if(b[i]==1):
        k+=1
    else:
        k=0
    c=max(c,k)
print(c)
