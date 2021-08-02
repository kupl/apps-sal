import bisect
n, m = [int(x) for x in input().split(" ")]
a = [int(x) for x in input().split(" ")]
b = [int(x) for x in input().split(" ")]

a = sorted(a)
max = a[n - 1]
min = a[0]
res = []


for i in range(0, m):
    if b[i] >= max:
        b[i] = n
    else:
        b[i] = bisect.bisect_right(a, b[i])

print(" ".join([str(x) for x in b]))
