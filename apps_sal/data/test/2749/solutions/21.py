h, w = list(map(int, input().split()))
n = int(input())
a = list(map(int, input().split()))

l = [[] for _ in range(h)]
x = 0
y = 0
for i in range(n):
    for _ in range(a[i]):
        l[y].append(i + 1)
        x += 1
        if x == w:
            x = 0
            y += 1
for i in range(h):
    if i % 2 == 0: print((*l[i]))
    else: print((*reversed(l[i])))
