from itertools import combinations
from functools import reduce

n = int(input())
x = [0 for _ in range(5)]
for _ in range(n):
    s = input()
    if s[0] == "M":
        x[0] += 1
    if s[0] == "A":
        x[1] += 1
    if s[0] == "R":
        x[2] += 1
    if s[0] == "C":
        x[3] += 1
    if s[0] == "H":
        x[4] += 1

def f(a, b): return a*b

x = [n for n in x if n != 0]
ans = 0
for c in combinations(x, 3):
    ans += reduce(f, c)

print(ans)
