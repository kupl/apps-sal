while(1):
    try:
        n=int(input())
        a=list(map(int,input().split()))
        a.sort()
        print(a[n-1],end=" ")
        for i in range(1,n-1):
            print(a[i],end=" ")
        print(a[0])
    except EOFError:
        break
        
