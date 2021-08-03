from itertools import combinations
n = int(input())
s = []
for i in range(n):
    s.append(input()[0])

c = (
    s.count("M"),
    s.count("A"),
    s.count("R"),
    s.count("C"),
    s.count("H"),
)
a = sum(x * y * z for x, y, z in combinations(c, 3))
print(a, flush=True)
