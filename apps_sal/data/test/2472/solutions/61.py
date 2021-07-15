N=int(input())
task=[[]]*N
for i in range(N):task[i]=list(map(int,input().split()))
task.sort(key=lambda x: x[1])
t=0
for i in range(N):
    t+=task[i][0]
    if task[i][1]<t:
        print('No')
        return
print('Yes')
