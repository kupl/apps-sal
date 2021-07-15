from collections import deque
queue = deque()
ans=0
cou=1
n = int(input())
for j in range(2*n):
    a=input().split()
    if a[0] == 'add':
        queue.append(int(a[1]))
    else:
        if queue:
            if cou == queue[-1]:
                
                queue.pop()
            else:
                ans+=1
                queue=deque()
                
        cou+=1
print(ans)
            

