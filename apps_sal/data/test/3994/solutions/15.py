n = int(input())
t = [int(w) for w in input()]
aar = []
bar = []
for __ in range(n):
    a, b = map(int, input().split())
    aar.append(a)
    bar.append(b)

r = 0

for __ in range(500):
    r = max(r, sum(t))
    for i in range(n):
        a, b = aar[i], bar[i]
        if __ >= b and (__ - b) % a == 0: t[i] ^= 1

print(r)
