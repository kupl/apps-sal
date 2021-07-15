n=int(input())

def func(start,goal,t):
    distance=abs(start[0]-goal[0])+abs(start[1]-goal[1])
    if distance<=t and (t-distance)%2==0:
        return True
    return False
now=0
can=1
start=[0,0]
for i in range(n):
    t,x,y=[int(i) for i in input().split()]
    goal=[x,y]
    if not func(start,goal,t-now):
        can=0
        break
    else:
        start=goal
        now=t

if can==1:
    print("Yes")
else:
    print("No")

