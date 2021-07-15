
n = int(input())

x = []
y = []

ans = []

A = list(map(int, input().split()))

for i in range(n):
    
    if A[i] == 1:
        
        if y:
            
            ans += [[y.pop(), i + 1]]
        
        elif x:
            
            ans += [[x.pop(), i + 1]]
            ans += [[i + 1, i + 1]]
            
        else:
            
            ans += [[i + 1, i + 1]]
            
    elif A[i] == 2:
        
        
        
        if x:
            ans += [[x.pop(), i + 1]]
            ans += [[i + 1, i + 1]]
            
            
            
        else:
            ans += [[i + 1, i + 1]]
            
        
        y += [i + 1]
            
    elif A[i] == 3:
        
        
        if x:
            
            ans += [[x.pop(), i + 1]]
            ans += [[i + 1, i + 1]]
            
            
        else:
            ans += [[i + 1, i + 1]]
        
        x += [i + 1]
        
            
if x or y:
    
    print(-1)
    
else:
    
    print(len(ans))
    
    for Ans in ans:
        
        print(*Ans)
