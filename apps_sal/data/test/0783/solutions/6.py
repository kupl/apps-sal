n = int(input())
h = [int(i) for i in input().split()] + [0]
v = [0 for i in h]
for p in range(n, -1, -1):
    if p == n:
        v[p] = h[p]
    else:
        v[p] = max(v[p + 1], h[p])
print(' '.join(['%s' % max(0, v[i + 1] + 1 - h[i]) for i in range(n)]))
