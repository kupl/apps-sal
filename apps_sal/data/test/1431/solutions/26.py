N = int(input())
a = list(map(int,input().split()))
b = [0] * N
ans = 0 
from collections import deque        
ansL = deque()
for i in range(N):
    m = N - i 
    count = 0
    for k in range(1,N//m+1):
        count += b[m*k-1]
    if count % 2 != a[m-1]:
        b[m-1] = 1
        ans += 1
        ansL.appendleft(m)    
print(ans)
print((*ansL)) 
    


