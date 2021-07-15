from collections import Counter
n, c, v = int(input()), Counter(), 0
for x in map(int, input().split()):
    v += sum(c[2 ** i - x] for i in range(31))
    c[x] += 1
print(v)
