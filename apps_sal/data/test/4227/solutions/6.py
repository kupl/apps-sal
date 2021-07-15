from itertools import permutations

N, M = map(int, input().split())
path = [[False] * N for _ in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    path[a][b] = path[b][a] = True

    ans = 0
    for i in permutations(range(N), N):
        if i[0] == 0:
            for j in range(N):
                if j == N - 1:
                    ans += 1
                    break
                if not path[i[j]][i[j + 1]]:
                    break

print(ans)
