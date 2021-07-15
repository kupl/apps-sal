import sys
from collections import Counter


def gen(counter, skip):
    for c, n in counter:
        has = n // 2
        if skip > has:
            skip -= has
            has = 0
        elif skip > 0:
            has -= skip
            skip = 0
        for i in range(has):
            yield c


def gen_o(counter, take):
    for c, n in counter:
        for i in range(n % 2):
            yield c
    for c, n in counter:
        has = (n // 2) * 2
        if take > has:
            take -= has
        elif take > 0:
            has = take
            take = 0
        for i in range(has):
            yield c


N = int(next(sys.stdin))

s = next(sys.stdin).strip()
c = Counter(s)

even = 0
odd = 0
items = list(c.items())
for _, n in items:
    even += n // 2
    odd += n % 2
generator = gen(items, 0)
generator_o = gen_o(items, 0)

odd_c = odd
if odd == 0:
    print(1)
    front = [next(generator) for i in range(len(s) // 2)]
    fs = "".join(front)
    print(fs + fs[::-1])
else:
    skip = 0
    while even != 0 and even % odd != 0:
        skip += 1
        odd += 2
        even -= 1
    generator = gen(items, skip)
    generator_o = gen_o(items, skip * 2)
    print(odd)
    per = even // odd
    strs = []
    for i in range(odd):
        front = [next(generator) for i in range(per)]
        fs = "".join(front)
        strs.append(fs + next(generator_o) + fs[::-1])
    print(" ".join(strs))

