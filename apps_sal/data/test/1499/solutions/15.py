'__author__'=='deepak Singh Mehta) learning to code '





def __starting_point():
    n,m = map(int,input().split())
    assert(m>=1 and m<=(4*n))
    if m%2!=0: #odd
        k = (n*4)//2
        k += 1
        for i in range(1,(n*4)//2+1):
            if k<=m:
                print(k,end=' ')
                k += 1
            if i<=m:
                print(i,end=' ')
            
    else: #even
        k = (n*4)//2
        k += 1
        for i in range(1,(n*4)//2+1):
            if k<=m :
                print(k,end=' ')
                k += 1
            if i<=m:
                print(i,end=' ')

__starting_point()
