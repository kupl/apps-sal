import bisect
(n, m, k) = map(int, input().split())
(x, s) = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))
z1 = list(zip(a, b))
z2 = list(zip(c, d))
result = n * x
for (ai, bi) in z1:
    if bi > s:
        continue
    current = ai * n
    if current < result:
        result = current
    rest = s - bi
    idx = bisect.bisect_right(d, rest)
    if idx == 0:
        continue
    current = ai * (n - z2[idx - 1][0])
    if current < result:
        result = current
for (ci, di) in z2:
    if di > s:
        continue
    current = x * (n - ci)
    if current < result:
        result = current
print(result)
