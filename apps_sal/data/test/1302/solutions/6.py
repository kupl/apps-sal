n, k = map(int, input().split())

if n - k == 0:
    print(-1)

elif n - k == 1:
    for j in range(n):
        print(j + 1, end = ' ')
    
else: 
    print(n, end = ' ')

    for i in range(2, 2 + k):
        print(i, end = ' ')
      
    print(1, end = ' ')    
        
    for h in range(k + 3, n + 1):
        print(h - 1, end = ' ')

