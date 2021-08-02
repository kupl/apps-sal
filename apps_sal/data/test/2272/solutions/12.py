visited = [0 for i in range(110)]


def reset():
    nonlocal N, visited
    for i in range(N):
        visited[i] = 0


def dfs(s, e):
    # print(s,e)
    nonlocal N, nodes, visited
    if(s == e):
        return True
    if(visited[s] == 1):
        return False
    visited[s] = 1
    ans = False
    for i in range(N):
        if(i == s):
            continue
        a = nodes[s][0]
        b = nodes[s][1]
        c = nodes[i][0]
        d = nodes[i][1]
        if((c < a and a < d) or (c < b and b < d)):
            ans = ans or dfs(i, e)
    return ans


nodes = []
N = 0
M = int(input())
for k in range(M):
    com, u, v = tuple(int(i) for i in input().split())

    if(com == 1):
        V = [u, v]
        nodes.append(V)
        N += 1
    else:
        u -= 1
        v -= 1
        reset()
        if(dfs(u, v)):
            print("YES")
        else:
            print("NO")
