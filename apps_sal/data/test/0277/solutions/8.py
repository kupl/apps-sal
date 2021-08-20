(n, a, b) = [int(v) for v in input().split()]
a -= 1
b -= 1
r = 1
while True:
    nn = n // 2
    aa = a // 2
    bb = b // 2
    if aa == bb:
        print('Final!' if nn == 1 else r)
        break
    (n, a, b) = (nn, aa, bb)
    r += 1
