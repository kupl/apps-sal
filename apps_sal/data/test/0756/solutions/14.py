n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(n):
    if a[i]>c+15:
        break
    else:
        c=a[i]
c+=15
if c>90:
    c=90
print(c)
