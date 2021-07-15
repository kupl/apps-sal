import sys
import itertools
from collections import Counter
N = int(input())
name = []
for _ in range(N):
    a = input()
    name.append(a[0])
name = Counter(name)
kouho = []
kouho.append(name["M"])
kouho.append(name["A"])
kouho.append(name["R"])
kouho.append(name["C"])
kouho.append(name["H"])
name = []
for i in kouho:
    if i == 0:
        continue
    name.append(i)
total = sum(name)
seki = 1
for i in name:
    seki = seki*i
hikuseki = 1
for i in name:
    if i > 1:
        hikuseki = hikuseki*i

if len(name) < 3:
    print((0))
    return

seki = list(itertools.combinations(name, 3))
ans = 0
for i in seki:
    a, b, c = i
    ans += a*b*c
print(ans)

