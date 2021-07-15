n, l, p, v = int(input()), 0, 0, 0
for a in map(int, input().split()):
    l = l + 1 if a > p else 1
    if l > v:
        v = l
    p = a
print(v)
