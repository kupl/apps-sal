for _ in range(int(input())):
    x,n,m = list(map(int,input().split()))
    for i in range(n):
        if x>20:
            x = x//2
            x+=10
        else:
            break
    x = x-(m*10)
    if x<=0:
        print("YES")
    else:
        print("NO")
