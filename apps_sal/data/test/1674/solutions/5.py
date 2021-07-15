import re, math, decimal, bisect, collections
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]

n, k = viread()
d = viread()
s = list(read())
processed = 0
damage = 0
while (processed < n):
    damages = []
    c = s[processed]
    damages.append(d[processed])
    processed += 1
    while (processed < n and s[processed] == c):
        damages.append(d[processed])
        processed += 1
    if len(damages) > k:
        damages.sort()
        damage += sum(damages[len(damages) - k:])
    else:
        damage += sum(damages)
print(damage)
