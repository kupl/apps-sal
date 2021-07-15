from math import ceil
t=int(input())
for _ in range(t):
    n,d=map(int,input().split())
    x=int(ceil(d**0.5))
    if d<=n:
        print("YES")
        continue
    flag=0
    for i in range(1,x+1):
        if i+int(ceil(d/(i+1)))<=n:
            print("YES")
            flag=1
            break
    if flag==0:
        print("NO")
