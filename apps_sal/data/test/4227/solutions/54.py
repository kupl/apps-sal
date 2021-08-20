from itertools import permutations
(N, M) = list(map(int, input().split()))
l = [list(map(int, input().split())) for _ in range(M)]
graph = [[False] * (N + 1) for _ in range(N + 1)]
for (i, j) in l:
    graph[i][j] = True
    graph[j][i] = True
pattern = permutations(list(range(1, N + 1)))
cnt = 0
for i in pattern:
    flag = True
    if i[0] != 1:
        continue
    for j in range(N - 1):
        if graph[i[j]][i[j + 1]] == False:
            flag = False
            break
    if flag:
        cnt += 1
print(cnt)
