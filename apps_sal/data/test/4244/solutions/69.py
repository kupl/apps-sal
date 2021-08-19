N = int(input())
x = [int(i) for i in input().split()]
y = 0
d = 0
for n in x:
    y += n
z = y // N
if y / N - z >= 0.5:
    g = z + 1
else:
    g = z
for s in x:
    d += (s - g) ** 2
print(d)
