from itertools import product

n, m, x = map(int, input().split())

CA = [list(map(int, input().split())) for _ in range(n)]

ans = 10**12 + 1
for t in product([0, 1], repeat=n):  # (1, 0, 0)
    cost = 0
    understanding = [0] * m
    for i, b in enumerate(t):
        if b == 1:
            cost += CA[i][0]
            for j, a in enumerate(CA[i][1:]):
                understanding[j] += a
    if sum(True for u in understanding if u >= x) == m:
        ans = min(ans, cost)

if ans == 10**12 + 1:
    print(-1)
else:
    print(ans)
