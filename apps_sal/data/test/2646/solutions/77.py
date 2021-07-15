from collections import deque
n,m = list(map(int,input().split()))
load = [list(map(int,input().split())) for _ in range(m)]
goal = [[] for _ in range(n)]
for i in load:
    goal[i[0]-1].append(i[1]-1)
    goal[i[1]-1].append(i[0]-1)

q = deque([0])
ans = [-1 for _ in range(n)]
ans[0] = 0
while q:
    check = q.popleft()
    for j in goal[check]:
        if ans[j] == -1:
            ans[j] = check+1
            q.append(j)
if -1 in ans:
    print("No")
else:
    print("Yes")
    for p in range(1,n):
        print((ans[p]))

