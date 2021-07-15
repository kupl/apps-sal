n, m = list(map(int, input().split()))
d = [1] * n
s = set()
for i in range(m):
    a, b, c = list(map(int, input().split()))
    if a - 1in s:
        if d[a - 1] == 1:
            d[b - 1] = 2
            d[c - 1] = 3
        
        if d[a - 1] == 2:
            d[b - 1] = 1
            d[c - 1] = 3
        
        if d[a - 1] == 3:
            d[b - 1] = 1
            d[c - 1] = 2
    
    if b - 1 in s:
        if d[b - 1] == 1:
            d[a - 1] = 2
            d[c - 1] = 3
        
        if d[b - 1] == 2:
            d[a - 1] = 1
            d[c - 1] = 3
        
        if d[b - 1] == 3:
            d[a - 1] = 1
            d[c - 1] = 2
    
    if c - 1 in s:
        if d[c - 1] == 1:
            d[b - 1] = 2
            d[a - 1] = 3
        
        if d[c - 1] == 2:
            d[b - 1] = 1
            d[a - 1] = 3
        
        if d[c - 1] == 3:
            d[b - 1] = 1
            d[a - 1] = 2
    if a - 1 not in s and b - 1not in s and c - 1 not in s:
        d[a - 1] = 1
        d[b - 1] = 2
        d[c - 1] = 3
    s.add(a - 1)
    s.add(b - 1)
    s.add(c - 1)
        
print(*d)        
        
            
        

