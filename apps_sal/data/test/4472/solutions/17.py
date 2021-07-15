n=int(input())
a=input()
b=input()
c=int()
for i in range(n//2):
    v=a[i]
    u=a[n-i-1]
    x=b[i]
    y=b[n-i-1]
    if v==x:
        if u!=y:
            c+=1
    elif v==y:
        if u!=x:
            c+=1
    elif x==y:
        if u!=v:
            c+=1
    else:
        if u!=x and u!=y:
            c+=2
        else:
            c+=1
if n%2==1:
    if a[n//2]!=b[n//2]:
        c+=1
print(c)

