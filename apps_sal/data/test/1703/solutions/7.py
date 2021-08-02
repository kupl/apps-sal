from collections import defaultdict
from sys import stdin

all_in = stdin.read().splitlines()

n = int(all_in[0])
s = all_in[1:]

one = defaultdict(lambda: 0)
two = defaultdict(lambda: 0)

for el in s:
    I = 0
    min_ = 0

    for char in el:
        I += {'(': 1, ')': -1}[char]
        min_ = min(min_, I)

    if I >= 0 and min_ == 0:
        one[I] += 1

    if I <= 0 and min_ == I:
        two[I] += 1

ans = 0
for el in list(one.keys()):
    ans += one[el] * two[-el]

print(ans)
