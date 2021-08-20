import sys


def I():
    return [int(x) for x in sys.stdin.readline().split()]


(N, K) = I()
Z = [I() for _ in range(N)]
Z.sort()
INF = 10 ** 20
ans = INF
for i in range(N):
    for j in range(i + K - 1, N):
        l = sorted((t[1] for t in Z[i:j + 1]))
        ans_tmp = [(Z[j][0] - Z[i][0]) * (v - u) for (u, v) in zip(l, l[K - 1:])]
        ans = min(ans, *ans_tmp)
print(ans)
