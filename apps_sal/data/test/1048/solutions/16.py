from collections import Counter

n = int(input())
s = input()

d = Counter(s)


try:
    temp = min(d['U'], d['D'])
    d['U'] -= temp
    d['D'] -= temp
except KeyError:
    pass

try:
    temp = min(d['L'], d['R'])
    d['L'] -= temp
    d['R'] -= temp
except KeyError:
    pass

print(n - sum(list(d.values())))

