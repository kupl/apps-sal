k, x = [int(n) for n in input().split()]

if x + (k - 1) >= 1000000:
    r = 1000000
else:
    r = x + (k - 1)
if x - (k - 1) <= -1000000:
    l = -1000000
else:
    l = x - (k - 1)

print(' '.join([str(n) for n in range(l, r + 1)]))
