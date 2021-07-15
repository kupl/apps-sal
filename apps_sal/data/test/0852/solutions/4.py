import sys
input = sys.stdin.readline
 
t = int(input())
letters = 'abcdefghijklmnopqrst'
 
for _ in range(t):

    n,k,l = list(map(int,input().split()))
    d = list(map(int,input().split()))
    
    ll = []
    
    tot = len(d)
    
    while len(d) > 0:
        ddd = []
        c= 0 
        for el in d:
            ddd.append(el)
            c += 1
            if el + k <= l:
                d = d[c:]
                break
        
        for j in range(2*k):
            ok = 1
            for s in range(len(ddd)):
                modif = (j + s + 1) % (2*k)
                modif = min(modif, 2*k - modif)
                
                depth = ddd[s] + modif
                #if j==3:
                #    print(depth, j)
                if depth > l:
                    ok = 0
                    
            if ok==1:
                break
            
        ll.append(ok)
        
        if len(d)==tot:
            break
        
        tot = len(d)
    
    if min(ll) == 1:
        print('Yes')
    else:
        print('No')
    

