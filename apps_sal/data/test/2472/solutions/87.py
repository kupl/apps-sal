from itertools import accumulate
n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]
ab.sort(key=lambda x: x[1])
(a, b) = zip(*ab)
a = list(a)
b = list(b)
a = list(accumulate(a))
for (i, j) in zip(a, b):
    if i > j:
        print('No')
        break
else:
    print('Yes')
