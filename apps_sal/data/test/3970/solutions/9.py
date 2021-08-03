n, k = [int(x) for x in input().split()]
a = sorted([int(x) for x in input().split()])
s = set(a)
l = 0
for x in a:
    t = 1
    while x in s:
        l += t
        t = 1 - t
        s.remove(x)
        x *= k
print(l)
