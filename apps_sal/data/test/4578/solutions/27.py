n,x=list(map(int,input().split()))
mi=10**5+1
s=0
for _ in range(n):
    a=int(input())
    s+=a
    if a<=mi:mi=a
print((n+(x-s)//mi))

