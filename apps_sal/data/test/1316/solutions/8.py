n, k = list(map(int, input().split()))
s = input() + '|'

prev = ''
d = {}

for c in s:
    if c == prev:
        d[c][-1] += 1

    else:
        d[c] = d.get(c, []) + [1]
    prev = c

res = 0


def f(l):
    return sum(e // k for e in l)


for l in list(d.values()):
    res = max(res, f(l))

print(res)
