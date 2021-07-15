from textwrap import wrap

input()
s = input()
t = input()

r = int(1e9)
p = list()

for i in range(len(t) - len(s) + 1):
    f = [x != y for x, y in zip(t[i: i + len(s)], s)]
    g = f.count(True)

    if g < r:
        r = g
        p = [str(i + 1) for i, e in enumerate(f) if e]

print(r)
print(' '.join(p))
