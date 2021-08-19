from collections import Counter
(n, m) = list(map(int, input().split()))
words = Counter()
for _ in range(n + m):
    words[input()] += 1
mutual = len([x for x in words if words[x] > 1])
if mutual % 2:
    print('YES' if n >= m else 'NO')
else:
    print('YES' if n > m else 'NO')
