a=int(input())
b=list(map(int, input().split()))
m=max(b)
r=0
f=0
u=0
o=0
k=0
while f<=m:
    f=2**r
    r+=1
r-=1
for i in range(a):
    for j in range(r):
        if b[i]%(2**j)==0:
            if 2**j>o:
                o=2**j
for i in range(a):
    if b[i]%o==0:
        k+=1
print(o,k)

