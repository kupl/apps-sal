n = int(input())

p = [int(x) for x in input().split()]

c = [[] for _ in range(n)]

t = 0

for i, x in enumerate(p):
    c[x].append(i)

res = []

while True:
    while t < n and len(c[t]) == 0 and t > 0:
        t -= 3
    if t >= n or len(c[t]) == 0:
        break
    res.append(c[t].pop() + 1)
    t += 1

if all(len(x) == 0 for x in c):
    print("Possible")
    print(" ".join(map(str, res)))
else:
    print("Impossible")
