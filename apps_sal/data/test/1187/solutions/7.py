n, m = map(int, input().split())
L = []
for i in range(n):
    s = []
    L.append(s)

st = []
for i in range(m):
    u, v = map(int, input().split())
    st.append((u - 1, v - 1))
    L[u - 1].append(v - 1)

visited = [False] * n
rs = [False] * n


def dfs(u):
    if(visited[u] == False):
        visited[u] = True
        rs[u] = True
        for i in L[u]:
            if(visited[i] == False and dfs(i) == True):
                return True
            elif(rs[i] == True):
                return True

    rs[u] = False
    return False


flag = 0
for i in range(0, n):
    if(dfs(i) == True):
        flag = 1
        break


if(flag == 0):
    print(1)
    for i in range(m):
        print(1, end=" ")
    print(" ")

else:
    print(2)
    for i in range(0, len(st)):
        if(st[i][0] < st[i][1]):
            print(1, end=" ")
        else:
            print(2, end=" ")
    print(" ")
