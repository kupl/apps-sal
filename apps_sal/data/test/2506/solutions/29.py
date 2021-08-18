import bisect
n, m = list(map(int, input().split()))
l = list(map(int, input().split()))
l.sort()
r = [0] * (10**5 + 2)
for i in range(n):
    r[l[i]] += 1
for i in range(10**5 + 1):
    r[i + 1] += r[i]
ok = 10**6
ng = 0
while ok - ng > 1:
    x = (ok + ng) // 2
    k = 0
    for i in range(n):
        if x - l[i] < 0:
            k += n
        elif x - l[i] > 10**5 + 1:
            k += 0
        else:
            k += n - r[x - l[i]]
    if k >= m:
        ng = x
    else:
        ok = x
p = [0] * (n + 1)
for i in range(n):
    p[i + 1] = p[i] + l[i]
ans = 0
mi = 0
for i in range(n):
    li = bisect.bisect_left(l, ok - l[i])
    ans += l[i] * (n - li) + p[n] - p[li]
    mi += n - li
print((ans - (mi - m) * ok))
