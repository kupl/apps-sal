n = int(input())
if n % 2 == 1:
    print(-1)
else:
    edges = [[] for i in range(n)]
    for i in range(n - 1):
        [a, b] = [int(j) for j in input().split()]
        edges[a - 1].append(b - 1)
        edges[b - 1].append(a - 1)
    dfs_stack = [0]
    c = [1 for i in range(n)]
    visited = [-1 for i in range(n)]
    visited[0] = 0

    while dfs_stack != []:
        current_node = dfs_stack[-1]
        can_go_further = False
        for i in edges[current_node]:
            if visited[i] == -1:
                dfs_stack.append(i)
                visited[i] = current_node
                can_go_further = True
        if can_go_further == False:
            dfs_stack.pop(-1)
            c[visited[current_node]] += c[current_node]

    ans = 0
    for i in c[1:]:
        if i % 2 == 0:
            ans += 1
    print(ans)
