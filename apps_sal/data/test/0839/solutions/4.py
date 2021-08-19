import itertools


def calc(comb):
    if len(comb) < 2:
        return 0
    s = 0
    for i in range(0, len(comb) // 2 * 2, 2):
        (a, b) = comb[i:i + 2]
        s += m[a, b] + m[b, a]
    return s + calc(comb[1:])


m = {}
for y in range(5):
    for (x, v) in enumerate(str.split(input())):
        m[x, y] = int(v)
print(max(list(map(calc, itertools.permutations(list(range(5)))))))
