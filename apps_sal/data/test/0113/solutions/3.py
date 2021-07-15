a,b=list(map(int,input().split()))
for i in range(b):
    if a%2==0:
        a//=2
    if a%5==0:
        a//=5
b=10**b
print(a*b)

