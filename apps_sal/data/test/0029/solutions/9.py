import sys


def debug(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


a = [int(ch) for ch in input()]
assert len(a) == 6
b1 = a[0:3]
b2 = a[3:6]
if sum(b1) > sum(b2):
    (b1, b2) = (b2, b1)
diff = sum(b2) - sum(b1)
deltas = sorted([9 - x for x in b1 if x < 9] + [x for x in b2 if x > 0], reverse=True)
cum_deltas = [0] + deltas[:]
for i in range(1, len(cum_deltas)):
    cum_deltas[i] += cum_deltas[i - 1]
for (i, x) in enumerate(cum_deltas):
    if cum_deltas[i] >= diff:
        break
print(i)
