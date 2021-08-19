import bisect
(n, m) = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
a.sort()
for i in range(m):
    print(bisect.bisect_right(a, b[i]), end=' ')
