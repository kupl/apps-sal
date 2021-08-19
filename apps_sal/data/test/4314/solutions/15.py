H, W = map(int, input().split())
A = []
for i in range(H):
    x = input()
    if x.count('#') == 0:
        continue
    A.append(x)

c = set()
for a in A:
    for i in range(W):
        if a[i] == '#':
            c.add(i)

for a in A:
    for i in range(W):
        if i in c:
            print(a[i], end='')
    print()
