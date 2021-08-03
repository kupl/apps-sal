from itertools import combinations_with_replacement as c
N, M, Q = map(int, input().split())
l1 = list(list(map(int, input().split())) for _ in range(Q))

ans = 0

for l2 in c(range(1, M + 1), N):
    total = 0
    for i in range(Q):
        if l2[l1[i][1] - 1] - l2[l1[i][0] - 1] == l1[i][2]:
            total += l1[i][3]
    ans = max(ans, total)

print(ans)
