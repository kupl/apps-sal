import sys

n, m = [int(i) for i in sys.stdin.readline().split()]
to_sets = [set() for _ in range(n)]
from_sets = [set() for _ in range(n)]
for i in range(m):
    m1, m2 = [int(i) for i in sys.stdin.readline().split()]
    to_sets[m1 - 1].add(m2 - 1)
    from_sets[m2 - 1].add(m1 - 1)

bd_choices_cache = [[0 for _ in range(n)] for _ in range(n)]
for a in range(n):
    for b in to_sets[a]:
        for c in to_sets[b]:
            bd_choices_cache[a][c] += 1

ans = 0
for a in range(n):
    for c in range(n):
        if a == c:
            continue
        bd_choices = bd_choices_cache[a][c]
        ans += bd_choices * (bd_choices - 1) // 2

print(ans)
