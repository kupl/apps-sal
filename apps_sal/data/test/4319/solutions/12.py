
def I(): return [int(i) for i in input().split()]


n, = I()
l = I() + [1]
a = []
for i in range(n):
    if l[i + 1] == 1:
        a.append(l[i])
print(l.count(1) - 1)
print(*a)
