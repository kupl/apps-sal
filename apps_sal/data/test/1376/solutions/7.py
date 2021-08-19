n = int(input())
a = list(map(int, input().split()))
p1 = 0
p2 = 0
total = 0
pos = {}
for i in range(n):
    pos[i] = []
for (i, val) in enumerate(a):
    pos[val - 1].append(i)
for i in range(n):
    (d1, d2) = pos[i]
    if p1 > p2:
        (p1, p2) = (p2, p1)
    total += abs(p1 - d1)
    total += abs(p2 - d2)
    (p1, p2) = (d1, d2)
print(total)
