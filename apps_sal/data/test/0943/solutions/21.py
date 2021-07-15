input()
ar = list(map(int, input().split()))

a = []
b = []
for t in ar:
    if t % 2 == 0:
        a.append(t)
    else:
        b.append(t)

b.sort()
if len(b) % 2 != 0:
    b = b[1:]

print(sum(a) + sum(b))
