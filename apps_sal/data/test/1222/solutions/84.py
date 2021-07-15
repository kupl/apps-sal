from collections import deque

K = int(input())

q = deque()
for i in range(1,10):
    q.append(i)
ans=0
cnt=0
while cnt<K:
    cnt+=1
    current = q.popleft()

    dn = [-1,0,1]
    for i in dn:
        if current%10+i<0 or current%10+i>9:
            continue
        q.append(current*10+current%10+i)
else:
    ans=current
    
print(ans)
