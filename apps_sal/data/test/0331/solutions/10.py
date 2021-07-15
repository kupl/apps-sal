n, m, k = [ int(x) for x in input().split() ]
a = [ int(x) for x in input().split() ]

m -= 1

r = 1000000

for i, x in enumerate(a):
    if 0 < x <= k:
        r = min(r, abs(i - m) * 10)

print(r)

