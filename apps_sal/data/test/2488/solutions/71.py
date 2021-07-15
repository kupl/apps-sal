#problems2
#silver fox vs monster
import math
N,D,A=map(int,input().split())
d=[]
for _ in range(N):
    x,h=map(int,input().split())
    d.append((x,h))
d.sort(key=lambda x:x[0])

now_damage=0
from collections import deque
d=deque(d)
ans=0
d_field=deque()
while d:
    x=d.popleft()
    place,life=x
    if d_field:
        while (d_field and d_field[0][0]<place) :
            now_damage-=A*d_field[0][1]
            d_field.popleft()      
    if life<=now_damage:
        pass
    elif life>now_damage:
        K=math.ceil((life-now_damage)/A)
        ans+=K
        now_damage+=K*A
        d_field.append((2*D+place,K))        
print(ans)
