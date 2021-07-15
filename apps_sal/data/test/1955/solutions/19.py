n, m = map(int, input().split())
d = list(map(int, input().split()))
a = list(map(int, input().split()))
def check(l):
    cur = [0] * m
    ans = 0
    
    for i in range(1, l):
        
        if d[i] > 0:
            cur[d[i] - 1] += 1
            
       
    fr = 1
    
    if cur.count(0) == 0:
        for i in range(1, l):
            if d[i] > 0:
                if cur[d[i] - 1] > 1:
                    fr += 1
                    cur[d[i] - 1] -= 1
                elif cur[d[i] - 1] == 1:
                    if a[d[i] - 1] <= fr:
                        fr -= a[d[i] - 1]
                        cur[d[i] - 1] = 0
            else:
                fr += 1
        if cur.count(0) == m:
            
            return(1)
            
        else:
            
            return(0)
            
    
        
    else:
       
        return(0)
    
    
    
    
def bins():
    l = sum(a) + m - 1
    r = n + 1
    while r > l + 1:
        z = (r + l) // 2
       
        if check(z) == 1:
            r = z
        else:
            l = z
        
    if r > n :
        print(-1)
    else:
        print(r)
bins()
