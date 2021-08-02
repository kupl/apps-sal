from collections import defaultdict
import itertools

n = int(input())
r = defaultdict(int)
for i in range(n):
    r[input()[0]] += 1

ans = 0
for c in itertools.combinations(list('MARCH'), 3):
    a = 1
    for cc in c:
        a *= r[cc]
    ans += a
print(ans)
