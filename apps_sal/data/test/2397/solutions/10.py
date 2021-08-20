import math
(n, k) = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = []
a.reverse()
counter = 0
for i in range(n - 1):
    counter += a[i]
    b.append(counter)
b.sort(reverse=True)
print(sum(b[:k - 1]) + sum(a))
