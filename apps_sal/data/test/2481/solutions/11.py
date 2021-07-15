from collections import defaultdict

H, W = list(map(int, input().split()))

V = 10

dists = []

for _ in range(V):
    dists.append(list(map(int, input().split())))

count = defaultdict(int)

for _ in range(H):
    for i in map(int, input().split()):
        count[i] += 1

for k in range(V):
    for i in range(V):
        for j in range(V):
            dists[i][j] = min(dists[i][j], dists[i][k] + dists[k][j])


ans = 0

for k, v in list(count.items()):
    if k == -1 or k == 1:
        continue
    ans += v * dists[k][1]
print(ans)


