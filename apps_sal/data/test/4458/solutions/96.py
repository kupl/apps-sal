n=int(input())
a=list(map(int,input().split()))
c=0
j=float('inf')
for i in a:
    if i<j:
        c+=1
    j=min(j,i)
print(c)
