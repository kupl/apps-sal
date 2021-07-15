from itertools import permutations
n, C = map(int, input().split())
d = [list(map(int, input().split())) for i in range(C)]
c = [list(map(int, input().split())) for i in range(n)]
l = [[0] * C for i in range(3)]
for i in range(n):
    for j, k in enumerate(c[i]):
        l[(i + j) % 3][k - 1] += 1
ans = float("inf")
for i in permutations(range(C), 3):
    cnt = 0
    for j in range(3):
        for k in range(C):
            cnt += d[k][i[j]] * l[j][k]
    ans = min(ans, cnt)
print(ans)
