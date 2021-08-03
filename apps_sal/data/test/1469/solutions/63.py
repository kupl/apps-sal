L = int(input())

paths = []
n = 2
v = 1
while n <= L:
    paths.append((v, v + 1, 0))
    paths.append((v, v + 1, n // 2))
    v += 1
    n *= 2
n //= 2

vlast = v
nn = n
ll = L - n

while ll > 0:
    if ll >= n:
        paths.append((v, vlast, nn))
        ll -= n
        nn += n
    n //= 2
    v -= 1

print((vlast, len(paths)))
for e in paths:
    print((*e))
