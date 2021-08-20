from bisect import bisect
(n, q) = map(int, input().split())
a = list(map(int, input().split()))
a.reverse()
s = sum(a)
for i in range(1, n):
    a[i] += a[i - 1]
k = list(map(int, input().split()))
tmp = 0
for i in range(q):
    tmp += k[i]
    if tmp >= s:
        tmp = 0
    print(bisect(a, s - tmp - 1) + 1)
