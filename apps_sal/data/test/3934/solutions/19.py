from collections import Counter
n = int(input())
counter = Counter()
for i in range(n - 1):
    (a, b) = map(int, input().split())
    counter.update([a, b])
if 2 in counter.values():
    print('NO')
else:
    print('YES')
