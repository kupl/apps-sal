n=int(input())
a=list(map(int,input().split()))
if a[0]>a[1]:
    i=0
    j=1
else:
    j=0
    i=1
for k in range(2,n):
    if a[k]>a[i]:
        j=i
        i=k
    elif a[k]>a[j]:
        j=k
print(i+1,a[j])
