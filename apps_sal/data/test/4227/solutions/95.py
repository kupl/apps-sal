from itertools import permutations

N, M = map(int, input().split())
Alist = [list(map(int, input().split())) for i in range(M)]

graph = [[False] * (N + 1) for i in range(N + 1)]

for i, j in Alist:
    graph[i][j] = True
    graph[j][i] = True

route = permutations(range(1, N + 1))

count = 0
for i in route:
    flag = True
    if i[0] != 1:
        continue
    for j in range(N - 1):
        if graph[i[j]][i[j + 1]] == False:
            flag = False
            break

    if flag == True:
        count += 1

print(count)
