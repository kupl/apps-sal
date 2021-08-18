n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))
graph = [[False] * (m + n) for _ in range(m + n)]
for i in range(n):
    for j in range(m):
        if(abs(arr1[i] - arr2[j]) <= 1):
            graph[i][j + n] = True
            graph[j + n][i] = True
u = [False] * (m + n)
to = [-1] * m


def match(v1):
    i = 0
    if u[v1]:
        return 0
    u[v1] = True
    for i2 in range(m):
        if(graph[v1][i2 + n] and (to[i2] == -1 or match(to[i2]))):
            to[i2] = v1
            return 1
    return 0


res = 0
for i1 in range(n + m):
    u = [False] * (m + n)
    res += match(i1)
print(res)
