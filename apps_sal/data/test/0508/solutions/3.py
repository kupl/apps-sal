n, a = list(map(int,input().split()))
S = (n-2)*180
v1=2
v2=1
v3=0
k=2
u=0
mi=180
for i in range(2, n):
    k+=1
    u=((k-2)*(180-(n-2)*180/n))/2
    if abs(a-u)<mi:
        mi=abs(a-u)
        v3=i+1
print(v1,v2,v3)

