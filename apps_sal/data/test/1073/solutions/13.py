n = int(input())
ans = 0
s = input()
for i in range(n):
    pl = [0, 0]
    st = [0, 0]
    if s[i] == 'U':
        pl[0] += 1
                
    if s[i] == 'D':
        pl[0] -= 1
                
    if s[i] == 'R':
        pl[1] += 1
                
    if s[i] == 'L':
        pl[1] -= 1
    for j in range(i + 1, n):
        
        if s[j] == 'U':
            pl[0] += 1
        
        if s[j] == 'D':
            pl[0] -= 1
        
        if s[j] == 'R':
            pl[1] += 1
        
        if s[j] == 'L':
            pl[1] -= 1
        if st == pl:
            ans += 1
print(ans)   
            
            
        

