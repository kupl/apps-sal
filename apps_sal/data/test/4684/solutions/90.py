r,g,b=map(int,input().split())

rgb=r*100+g*10+b
if rgb%4==0:
    print("YES")
else:
    print("NO")
