(n, d) = (int(x) for x in input().split())
ps = sorted([int(x) for x in input().split()])
r = 1000
for st in range(1, 110):
    fn = st + d
    rr = len([x for x in ps if x < st or x > fn])
    if rr < r:
        r = rr
print(r)
