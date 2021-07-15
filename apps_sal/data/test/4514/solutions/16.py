def dfs(dp,node,edges,order):
    visited = set()
    stack = [node]
    while stack:
        curr = stack[-1]
        if curr not in visited:
            visited.add(curr)
            order.append(curr)
            
        count = 0
        for kid in edges[curr]:
            if kid in visited:
                count += 1
            else:
                stack.append(kid)

        if count == len(edges[curr]):
            stack.pop()
            for kid in edges[curr]:
                dp[curr] += dp[kid]

            dp[curr] += 1

        #print(stack)
            

def solve(u,k,dp,order,indices,ans):
    if k > dp[u]:
        ans.append(-1)
        return

    index = indices[u]
    ans.append(order[index+k-1])

def main():
    n,q = list(map(int,input().split()))
    parents = list(map(int,input().split()))
    edges = {}
    for i in range(1,n+1):
        edges[i] = []

    for i in range(2,n+1):
        parent = parents[i-2]
        edges[parent].append(i)

    for i in list(edges.keys()):
        edges[i].sort(reverse = True)

    indices = [-1]*(n+1)
    order = []
    dp = [0]*(n+1)
    dfs(dp,1,edges,order)
    #print(order)
    #print(dp)
    for i in range(n):
        indices[order[i]] = i

    ans = []
    for i in range(q):
        u,k = list(map(int,input().split()))
        solve(u,k,dp,order,indices,ans)

    for i in ans:
        print(i)


main()

