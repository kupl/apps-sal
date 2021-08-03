import bisect
n, k = list(map(int, input().split()))
r, o = list(map(int, input().split())), ''
d = {}
for i in range(k):
    a, b = list(map(int, input().split()))
    if [b] != d.setdefault(a, [b]):
        d[a] += [b]
    if [a] != d.setdefault(b, [a]):
        d[b] += [a]
rr = sorted(r)
for i in range(1, n + 1):
    a = bisect.bisect_left(rr, r[i - 1])
    if i in d:
        for j in d[i]:
            if r[j - 1] < r[i - 1]:
                a -= 1
    o += str(a) + ' '
print(o)
