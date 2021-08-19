from collections import defaultdict
n = int(input())
D1 = defaultdict(int)
D2 = defaultdict(int)
for i in range(n):
    (x, y) = [int(x) for x in input().split()]
    D1[x + y] += 1
    D2[x - y] += 1
print(sum((D1[k] * (D1[k] - 1) // 2 for k in D1)) + sum((D2[k] * (D2[k] - 1) // 2 for k in D2)))
