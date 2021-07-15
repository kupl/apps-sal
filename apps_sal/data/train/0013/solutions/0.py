for i in range(int(input())):
    n,g,b=map(int,input().split())
    nn=(n+1)//2
    print(max(nn+(nn-1)//g*b,n))
