import bisect

n, q = list(map(int, input().split()))
a = list(map(int, input().split()))
s = [0, ]
for i in a:
    s.append(s[-1] + i)

k = list(map(int, input().split()))
tb = 0
for i in range(q):
    tb += k[i]
    if tb >= s[-1]:
        tb = 0
        print(n)
    else:
        ans = bisect.bisect_right(s, tb)
        print(n - ans + 1)
