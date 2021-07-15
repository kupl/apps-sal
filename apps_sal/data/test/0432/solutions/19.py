def dfs(node,edges,costs,visited):
    cycle = False
    visited1 = set()
    while True:
        if node in visited:
            for i in visited1:
                visited.add(i)
            return 0
        if not edges[node]:
            visited1.add(node)
            break
        if node not in visited1:
            visited1.add(node)
            node = edges[node][0]
        else:
            cycle = True
            break

    #print(node,cycle,visited)
    if cycle:
        x = edges[node][0]
        min_cost = costs[x-1]
        while x != node:
            x = edges[x][0]
            min_cost = min(min_cost,costs[x-1])
        cost = min_cost
    else:
        cost = costs[node-1]

    for i in visited1:
        visited.add(i)

    return cost
    

def solve(zero,edges,costs):
    n = len(costs)
    visited = set()
    cost = 0

    for i in range(1,n+1):
        if i not in visited:
            cost += dfs(i,edges,costs,visited)

    print(cost)

def main():
    n = int(input())
    costs = list(map(int,input().split()))
    mouse = list(map(int,input().split()))
    edges = {}
    for i in range(1,n+1):
        edges[i] = []

    indegree = [0]*(n+1)
    for i in range(1,n+1):
        if i != mouse[i-1]:
            edges[i].append(mouse[i-1])
            indegree[mouse[i-1]] += 1

    zero = []
    for i in range(1,n+1):
        if indegree[i] == 0:
            zero.append(i)

    solve(zero,edges,costs)


main()

