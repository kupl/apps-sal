n,a = list(map(int,input().split()))
k = 0
for i in range(1,n,2):
    k+=1
    if i==a:
        print(k)
k = 0
for i in range(n,1,-2):
    k+=1
    if i==a:
        print(k)

