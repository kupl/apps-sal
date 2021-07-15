def parser():
    return [int(x) for x in input().split(" ")]

def DFS():
    visited[0]=True
    stack=[]
    intruduction_order=[]
    stack.append(0)
    while len(stack)>0:
        v=stack.pop()
        for u in adjacents_list[v]:
            if not visited[u]:
                pi[u]=v
                visited[u]=True
                if university_in_city[u]:
                    count_universities_subtree[u]+=1
                stack.append(u)
                intruduction_order.append(u)
    for v in intruduction_order[::-1]:
        count_universities_subtree[pi[v]]+=count_universities_subtree[v]


n,k=parser()
visited=[False for x in range(n)]
pi=[0 for x in range(n)]
count_universities_subtree=[0 for x in range(n)]
university_in_city=[False for x in range(n)]

cities_universities=parser()
for i in range(2*k):
    university_in_city[cities_universities[i]-1]=True

adjacents_list=[[] for x in range(n)]
for i in range(n-1):
    edge=parser()
    adjacents_list[edge[0]-1].append(edge[1]-1)
    adjacents_list[edge[1]-1].append(edge[0]-1)

DFS()

total=0

for i in range(1,n):
    total+=min(count_universities_subtree[i],2*k-count_universities_subtree[i])

print(total)
