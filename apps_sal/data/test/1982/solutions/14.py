for i in range(int(input())):
    n,k=map(int,input().split())
    if (k%2)^(n%2)==0:
        if n>=k**2:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
