a = 1
d = 10**18
for i in [*open(0)][1].split():
    a = min(a * int(i), d + 1)
print([a, -1][a > d])
