
n=int(input())
a=list(map(int, input().split()))
b=0

for i in range(0,n):
    if a[i]%2==0:
        if a[i]%3==0 or a[i]%5==0:
            b+=1
        else:
            b-=1000
            
if b>=0:
    print("APPROVED")
else:
    print("DENIED")



