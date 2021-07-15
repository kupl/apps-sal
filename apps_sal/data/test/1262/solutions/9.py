import sys

reader = (list(map(int, s.split())) for s in sys.stdin)
 
n, = next(reader)
xy = []
for _ in range(n):
    x, y = next(reader)
    xy.append([x, y])
c = list(next(reader))
k = list(next(reader))


# n = int(input())
# xy = [[]]*n
# for i in range(n):
#     xy[i] = list(map(int,input().split()))

# c = list(map(int,input().split()))
# k = list(map(int,input().split()))

graph = [[0 for _ in range(n+1)] for _i in range(n+1)]

for i in range(n):
    for j in range(i+1,n):
        cost = (abs(xy[i][0]-xy[j][0])+abs(xy[i][1]-xy[j][1]))*(k[i]+k[j])
        graph[i][j] = graph[j][i] = cost
    graph[n][i] = graph[i][n] = c[i]

# def output(parent):
#     es = []
#     vs = []
#     cost = 0
#     for i in range(1,(n+1)):
#         if parent[i]==n:
#             vs.append(i+1)
#         elif i==n:
#             vs.append(parent[i]+1)
#         else:
#             es.append([i+1,parent[i]+1])
#         cost+= graph[i][parent[i]]
#     print(cost)
#     print(len(vs))
#     print(*vs)
#     print(len(es))
#     for i in es:
#         print(i[0],i[1])
            

# def minKey(key, mstSet): 
#     # Initilaize min value 
#     min = 1000000000000 

#     for v in range((n+1)): 
#         if key[v] < min and mstSet[v] == False: 
#             min = key[v] 
#             min_index = v 

#     return min_index 

def primMST():
    # Key values used to pick minimum weight edge in cut 
    key = [1000000000000] * (n+1)
    parent = [None] * (n+1) # Array to store constructed MST 
    # Make key 0 so that this vertex is picked as first vertex 
    key[0] = 0 
    mstSet = [False] * (n+1) 

    parent[0] = -1 # First node is always the root of 

    for cout in range((n+1)): 

        # Pick the minimum distance vertex from  
        # the set of vertices not yet processed.  
        # u is always equal to src in first iteration 
        mn = 1000000000000 

        for v in range((n+1)): 
            if key[v] < mn and mstSet[v] == False: 
                mn = key[v] 
                min_index = v 

        u = min_index 

        # Put the minimum distance vertex in  
        # the shortest path tree 
        mstSet[u] = True

        # Update dist value of the adjacent vertices  
        # of the picked vertex only if the current  
        # distance is greater than new distance and 
        # the vertex in not in the shotest path tree 
        for v in range((n+1)): 
            # graph[u][v] is non zero only for adjacent vertices of m 
            # mstSet[v] is false for vertices not yet included in MST 
            # Update the key only if graph[u][v] is smaller than key[v] 
            if graph[u][v] > 0 and mstSet[v] == False and key[v] > graph[u][v]: 
                    key[v] = graph[u][v] 
                    parent[v] = u
        
    # es = []
    vss = 0
    # vs = []
    cost = 0
    for i in range(1,(n+1)):
        if parent[i]==n or i==n:
            vss += 1
        #     vs.append(i+1)
        # elif i==n:
        #     vs.append(parent[i]+1)
        # else:
        #     es.append([i+1,parent[i]+1])
        cost+= graph[i][parent[i]]
    
    myprint = sys.stdout.write

    myprint(str(cost) + '\n')
    # print(cost)
    # print(vss)
    myprint(str(vss)+'\n')
    

    vs = [0]*(vss)
    es = [[]]*(n-vss)
    k1,k2 = 0,0

    for i in range(1,(n+1)):
        if parent[i]==n:
            vs[k1] = i+1
            k1+=1
        elif i==n:
            vs[k1] = parent[i]+1
            k1+=1
        else:
            es[k2] = [i+1,parent[i]+1]
            k2+=1
        # cost+= graph[i][parent[i]]

    # print(*vs)
    [myprint(str(st) + ' ') for st in vs]
    myprint('\n')
    myprint(str(len(es))+'\n')
    [myprint(str(i[0]) + ' ' + str(i[1]) + '\n') for i in es]
    # print(len(es))
    # for i in es:
    #     print(i[0],i[1])
        
    
    
    # myprint(str(totalCost) + '\n')
    # myprint(str(len(stations)) + '\n')
    # [myprint(str(st) + ' ') for st in stations];
    # myprint(str(len(connections)) + '\n')
    # [myprint(str(c1) + ' ' + str(c2) + '\n') for c1, c2 in connections];


primMST()

# e = 0
# i=0
# ans = []
# ret = 0
# while e<n:
#     edge = edges[i]
#     i+=1
#     cost,a,b = edge
#     if find(a)!=find(b):
#         e+=1
#         ans.append([cost,a,b])
#         union(a,b)
#         ret += cost

# vs = []
# es = []
# for i in ans:
#     if i[1]==n:
#         vs.append(i[2]+1)
#     else:
#         es.append(i)

# print(ret)
# print(len(vs))
# print(*vs)
# print(len(es))
# for i in es:
#     print(i[1]+1,i[2]+1)


