from bisect import bisect_left

n, m = list(map(int, input().split()))
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
t = [0]
s = 0
for x in a:
    s += x
    t.append(s)

for x in b:
    p = bisect_left(t, x)
    print(p, x - t[p - 1])

