from itertools import permutations
(n, m) = map(int, input().split())
v = [set() for _ in range(n)]
for i in range(m):
    (ai, bi) = map(int, input().split())
    v[ai - 1].add(bi - 1)
    v[bi - 1].add(ai - 1)
ans = 0
for ci in permutations(range(n)):
    if not ci[0]:
        for i in range(n - 1):
            if not ci[i + 1] in v[ci[i]]:
                break
        else:
            ans += 1
print(ans)
