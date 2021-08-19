import bisect
(n, m) = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
res = []
for i in range(m):
    res.append(bisect.bisect_right(a, b[i]))
print(' '.join(map(str, res)))
