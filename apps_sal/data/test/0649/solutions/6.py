k = int(input()) & 1
p = []
s = range(1, 6)
for q in map(int, input().split()[::-1]):
    if k:
        p += [(x, -y) for (x, y) in p]
        p = [(x - q, y) for (x, y) in p]
        p += [(-x, 0) for x in s[:q]]
    else:
        p += [(y, -x) for (x, y) in p]
        p = [(x - q, y + q) for (x, y) in p]
        p += [(-x, x) for x in s[:q]]
    p = list(set(p))
    k = 1 - k
print(len(p))
