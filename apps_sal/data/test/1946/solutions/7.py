elA = dict()
elAs = set()
elB = dict()
elBs = set()
s = 0
n = int(input())
for i in range(n):
    x, y = list(map(int, input().split()))
    elA[x] = y
    elAs.add(x)
m = int(input())
for i in range(m):
    x, y = list(map(int, input().split()))
    elB[x] = y
    elBs.add(x)
w = elAs & elBs
for k in w: s += max(elA[k], elB[k])
for k in elAs:
    if k not in w: s += elA[k]
for k in elBs:
    if k not in w: s += elB[k]
print(s)

