for _ in range(int(input())):
    x,y=list(map(int,input().split()))
    if x>=y:
        print("YES")
    elif x==2 and y>3:
        print("NO")
    elif x==1 and y>=2:
        print("NO")
    elif x==3 and y>3:
        print("NO")
    else:
        print("YES")

