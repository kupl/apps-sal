try:
    n=int(input())
    c=0
    l=list(map(int,input().split()))
    for i in range(n-1,0,-1):
        if(l[i]!=l[i-1]):
            print(i+1)
            c=1
            break
    if(c==0):
        print(1)
except EOFError:
    pass
    

