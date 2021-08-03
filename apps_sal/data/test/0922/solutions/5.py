n, a = list(map(int, str.split(input())))
ns = tuple(map(int, str.split(input())))
s = sum(ns)
res = []
for x in ns:

    low = max(0, a - (s - x) - 1)
    high = min(x, a - (n - 1))
    res.append(low + x - high)

print(str.join(" ", list(map(str, res))))
