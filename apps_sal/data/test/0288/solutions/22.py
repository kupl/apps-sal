n = int(input())
f = 2
g = 1
c = 0
while f <= n:
    (f, g) = (f + g, f)
    c += 1
print(c)
