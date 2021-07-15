n, m, x = list(map(int,input().split()))
a = list(map(int,input().split()))

goal_0 = 0
goal_1 = 0

for i in range(x,0,-1):
    if i in a:
        goal_0 += 1

for i in range(x,n+1,1):
    if i in a:
        goal_1 += 1

if goal_0 < goal_1:
    print(goal_0)
else:
    print(goal_1)

