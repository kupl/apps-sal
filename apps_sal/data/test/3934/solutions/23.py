from collections import defaultdict
n = int(input())
graph = defaultdict(list)
flag=0
for i in range(n-1):
    a,b = list(map(int,input().split()))
    graph[a].append(b)
    graph[b].append(a)
for j in range(1,n+1):
    if(len(graph[j])==2):
        flag=1
        break
if(flag==1):
    print("NO")
else:
    print("YES")
    

