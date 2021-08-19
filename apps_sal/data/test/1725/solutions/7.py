def polo(l, d):
    l.sort()
    k = l[int(len(l) / 2)]
    s = 0
    for n in l:
        if abs(n - k) % d == 0:
            s = s + abs(n - k)
        else:
            return -1
    return int(s / d)


l = []
(n, m, d) = [int(x) for x in input().split(' ')]
for _ in range(n):
    l.extend((int(x) for x in input().split(' ')))
print(polo(l, d))
