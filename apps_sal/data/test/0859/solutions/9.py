from itertools import chain

line = input()
p = line.count('+') - line.count('-')
d = [0]
for c in input():
    if c == '-':
        d = [x - 1 for x in d]
    elif c == '+':
        d = [x + 1 for x in d]
    else:
        d = list(chain.from_iterable((x + 1, x - 1) for x in d))
print(round(d.count(p) / len(d), 9))
