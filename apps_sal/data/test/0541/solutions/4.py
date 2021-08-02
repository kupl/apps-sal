from operator import itemgetter
N, M = map(int, input().split())
islands = [list(map(int, input().split())) for _ in range(M)]
islands.sort(key=itemgetter(1))

i = 0
cnt = 0
while i < M:
    j = 0
    while i + j < M and islands[i + j][0] < islands[i][1]:
        j += 1
    i += j
    cnt += 1
print(cnt)
