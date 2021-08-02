N, M = [int(x) for x in input().split()]
AB = [[int(x) for x in input().split()] for _ in range(M)]


x = set()
for a, b in AB:
    if a == 1:
        x.add(b)
    if b == 1:
        x.add(a)

f = False

for a, b in AB:
    if (a in x and b == N) or (b in x and a == N):
        f = True

if f:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
