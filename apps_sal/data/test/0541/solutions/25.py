x = c = 0
for (a, b) in sorted([list(map(int, o.split())) for o in open(0)][1:], key=lambda p: p[1]):
    if a > x:
        x = b - 1
        c += 1
print(c)
