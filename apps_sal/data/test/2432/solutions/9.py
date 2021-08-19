# And after happily lived ever they

n = int(input())
d = [0, 5, 3, 2, 4, 1]

r = 0
for dd in d:
    r = r * 2 + bool(n & 1 << (5 - dd))

print(r)
