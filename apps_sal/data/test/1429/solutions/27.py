from collections import Counter

n, s = input().split()
n = int(n)

d = Counter()

at, cg = 0, 0
d[(at, cg)] = 1
ans = 0

for x in s:
    if x == "A":
        at += 1
    elif x == "T":
        at -= 1
    elif x == "C":
        cg += 1
    else:
        cg -= 1
    ans += d[(at, cg)]
    d[(at, cg)] += 1
print(ans)
