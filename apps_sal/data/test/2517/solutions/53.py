from scipy.sparse.csgraph import floyd_warshall
import itertools


def warshal_floyd(d):
    # d[i][j] := iからjへの最短距離
    nonlocal N
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    # "今現在求まっているiからjへの最短距離"と"今現在求まっているiからkへの最短距離 + 今現在求まっているkからjへの最短距離 の和"を比較する
    return d


N, M, R = list(map(int, input().split()))  # N個の町, M本の道, R個の町を訪れることになった
town = list([int(x)-1 for x in input().split()])
distant = [[float('inf')]*N for _ in range(N)]
for _ in range(M):
    a, b, c = list(map(int, input().split()))
    a -= 1
    b -= 1
    distant[a][b] = c
    distant[b][a] = c
for i in range(N):
    distant[i][i] = 0
distant = floyd_warshall(distant)
# warshal_floyd(distant)
# print(distant)  # Rは最大8だから全てを試しても大丈夫
ans = 10**9
for x in itertools.permutations(town):
    x = list(x)
    now = x[0]
    tmp = 0
    for i in range(1, len(x)):
        tmp += distant[now][x[i]]
        now = x[i]
    ans = min(ans, tmp)
print((int(ans)))

