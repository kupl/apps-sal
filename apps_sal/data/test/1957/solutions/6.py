n,a,b=list(map(int,input().split()))
x=[int(x) for x in input().split()]
p=x[0]
d=sum(x)
x.remove(x[0])
c=0
x.sort(reverse=True)

for i in x:
    if((a*p)/d>=b):
        break
    else:
        d-=i
        c+=1
print(c)

