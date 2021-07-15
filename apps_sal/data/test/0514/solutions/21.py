import math
for _ in range(int(input())):
    n,d=map(int,input().split())
    if n>=d:
        print("YES")
    else:
        flag=0
        for i in range(1,int(d**0.5)+2,1):
            if i+math.ceil(d/(i+1))<=n:
                flag=1
                break
        if flag==1:
            print("YES")
        else:
            print("NO")
