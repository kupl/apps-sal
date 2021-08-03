N, M = map(int, input().split())
K = []
for i in range(N):
    K.append(list(map(int, input().split())))

K_list = []
for x in range(N):
    K[x].remove(K[x][0])
    K_list.extend(K[x])

cnt = 0
for j in range(1, M + 1):
    if K_list.count(j) == N:
        cnt += 1

print(cnt)
