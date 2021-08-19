from collections import Counter


def warshall_floyd(V):
    for k in range(V):
        for i in range(V):
            for j in range(V):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])


INF = float('inf')
(H, W) = list(map(int, input().split()))
d = [[int(i) for i in input().split()] for _ in range(10)]
a = []
for _ in range(H):
    a.extend([int(i) for i in input().split() if i != '-1'])
dic = Counter(a)
warshall_floyd(10)
ans = 0
for (key, val) in list(dic.items()):
    ans += d[key][1] * val
print(ans)
