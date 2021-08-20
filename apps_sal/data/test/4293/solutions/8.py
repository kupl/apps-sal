from itertools import permutations
pqr = list(map(int, input().split()))
ans = 100 * 3
for (i, j) in permutations(pqr, 2):
    ans = min(ans, i + j)
print(ans)
