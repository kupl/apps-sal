from collections import Counter
n = int(input())
d = Counter()
for _ in range(n - 1):
    (u, v) = list(map(int, input().split()))
    d[u] += 1
    d[v] += 1
if any((x == 2 for x in list(d.values()))):
    print('NO')
else:
    print('YES')
