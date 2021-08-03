n = int(input())
h = []
a = []
changes = 0
for i in range(n):
    x, y = map(int, input().split())
    h.append(x)
    a.append(y)

for i in h:
    changes += a.count(i)

print(changes)
