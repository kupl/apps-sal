import sys

    
def main():
    #n = iinput()
    #k = iinput() 
    #m = iinput() 
    n = int(sys.stdin.readline().strip()) 
    #n, k = rinput()
    #n, m = rinput()
    #m, k = rinput()
    #n, k, m = rinput()
    #n, m, k = rinput()
    #k, n, m = rinput()
    #k, m, n = rinput() 
    #m, k, n = rinput()
    #m, n, k = rinput()
    q = list(map(int, sys.stdin.readline().split()))
    #q = linput()
    clovar, p, x = {}, [], 1e9
    for i in range(n):
        if q[i] in clovar:
            clovar[q[i]].append(i)
        else:
            clovar[q[i]] = [i]
    for o in clovar:
        t = clovar[o]
        ma = max(t[0] + 1, n - t[-1])
        dlinat = len(t) - 1
        for i in range(dlinat): 
            ma = max(t[i + 1] - t[i], ma)
        p.append([ma, o])
    p.sort()
    ans = [p[0]]
    dlinap = len(p)
    for i in range(1, dlinap):
        if ans[-1][0] != p[i][0]:
            ans.append(p[i])
    ans.append([n + 1, 1e9])
    dlina_1 = ans[0][0] - 1
    print(*[-1 for i in range(dlina_1)], end=" ")
    dlinaans = len(ans) - 1
    for i in range(dlinaans):
        x = min(x, ans[i][1])
        dlinax = ans[i + 1][0] - ans[i][0]
        print(*[x for o in range(dlinax)], end=" ")
    print()
           
        
            
    
    
    
    
    
    
            
                
        
    
            
        

            
        
    
                
    
    
    
            
    
        
    

for i in range(int(sys.stdin.readline().strip()) ):
    main()
    

