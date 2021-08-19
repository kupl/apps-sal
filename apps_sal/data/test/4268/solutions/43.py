from itertools import combinations
(n, d) = map(int, input().split())
L = list((list(map(int, input().split())) for _ in range(n)))
C = list(combinations(L, 2))
ans = 0
for i in range(len(C)):
    total = 0
    for (a, b) in zip(C[i][0], C[i][1]):
        total += abs(a - b) ** 2
    if total ** 0.5 % 1 == 0:
        ans += 1
print(ans)
