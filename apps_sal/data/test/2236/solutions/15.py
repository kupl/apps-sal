from collections import Counter

c = Counter()
n = int(input())
a = list(map(int, input().split()))

for i in range(1, n):
    a[i] += a[i - 1]
c.update(a)

print(n - c.most_common()[0][1])
