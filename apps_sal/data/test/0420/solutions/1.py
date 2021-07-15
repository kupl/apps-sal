n,m=map(int,input().split())
a=[]
for i in range(n):
    a.append(''.join(input().split()))
while n%2==0:
    k=0
    for i in range(n//2):
        if a[i]==a[n-i-1]:
            k+=1
    if k!=n//2:
        break
    n=n//2
print(n)
