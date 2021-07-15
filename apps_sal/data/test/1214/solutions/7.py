def bi(a, x):
    l  = -1
    u  = len(a)
    
    while(u-l>1):
        md = int((l+u) / 2)
        if x >= a[md]:
            l = md
        else:
            u = md
    return u  

d = {}
for x in range(1, 100000):
    
    for a in range(1, 500):
        diff = a*a + 2*a*x
        
        if diff > 200000:
            break
        
        if diff  not in d:
            d[diff] = []
            
        d[diff].append(x*x)    
        
def solve(a, d):
    cur = 0
    ans = ''
    
    for x in a:
        if x not in d:
            return 'No', ''
        
        next_ = bi(d[x], cur)
        
        if next_ == len(d[x]): 
            return 'No', ''
        
        next_ = d[x][next_]
        ans  +=  str(next_ - cur) + ' ' + str(x) +' '
        cur = next_ + x 
    
    return 'Yes', ans

n   = int(input())
a   = list(map(int, input().split()))
ans = solve(a, d)

print(ans[0])
print(ans[1])
