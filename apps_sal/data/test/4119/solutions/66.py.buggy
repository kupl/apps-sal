n, m = list(map(int, input().split()))
x = list(map(int, input().split()))

if n >= m:
    print((0))
    return

x.sort()

dists = []
point = x.pop(0)
for xs in x:
    dists.append(xs - point)
    point = xs
dists.sort(reverse=True)

print((sum(dists[(n - 1):])))
