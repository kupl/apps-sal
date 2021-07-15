def ans():
    n, t= [int(i) for i in input().split()]
    a= [0]
    a+= [int(i) for i in input().split()]
    #print(a)
    
    ans= 1
    i= 1
    while True:
        ans+= a[i]
        i= ans
        if ans== t:
            print("YES")
            return
        
        if i> t:
            print("NO")
            return

ans()
