def solve():
    N = int(input())
    
    incr = []
    decr = []
    
    for i in range(1,N+1):
        a, b = map(int, input().split())
        
        if a > b:
            decr.append((a,b,i))
        else:
            incr.append((a,b,i))
            
    result1 = []
    result2 = []

    if decr:
        decr.sort(key = lambda x:x[1])
        
        result1.append(decr[0])
        
        for i in range(1, len(decr)):
            a, b, idx = decr[i]
            if a > result1[i-1][1]:
                result1.append((a,b,idx))
    
    if incr:
        incr.sort(key = lambda x:x[1])
        incr.reverse()

        result2.append(incr[0])
        
        for i in range(1, len(incr)):
            a, b, idx = incr[i]
            if a < result2[i-1][1]:
                result2.append((a,b,idx))

    if len(result1) > len(result2):
        print (len(result1))
        print (' '.join(str(k[2]) for k in result1))
    else:
        print (len(result2))
        print (' '.join(str(k[2]) for k in result2))
    
def __starting_point():  
    solve()    
__starting_point()
