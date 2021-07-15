import itertools
n = int(input())
s = list(input())
count = 0
values = {(l, r): next(iter(set("RGB") - {l, r})) for l, r in itertools.product("RGB", repeat=2)}
ranges = []
start = None
for i in range(1, n):
    if s[i - 1] == s[i]:
        if start is None:
            start = i - 1
    elif start is not None:
        ranges.append((start, i))
        start = None
if start is not None:
    ranges.append((start, n))

for r in ranges:
    for i in range(r[0] + 1, r[1], 2):
        l = s[i - 1]
        r = s[(i + 1) % n]
        s[i] = values[l, r]
        count += 1

print(count)
print("".join(s))

