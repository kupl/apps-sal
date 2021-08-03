import math


def next_sunuke(N):
    D = math.ceil(math.log(N, 10) + 1)
    z = str(N)
    zx = [int(z[:1]) for z in z]
    Z = N / sum(zx)
    ret_val = N
    ret_vals = [ret_val]
    for d in range(0, D):
        x = ((10 ** (d + 1)) * math.floor((N / (10 ** (d + 1))) + 1)) - 1
        w = str(x)
        sx = [int(w[:1]) for w in w]
        y = x / sum(sx)
        if y == Z:
            Z = y
            ret_vals.append(x)
        elif y < Z:
            Z = y
            ret_vals = []
            ret_vals.append(x)
    return min(ret_vals)


K = int(input())
n = 1
for i in range(1, K + 1):
    print((next_sunuke(n)))
    n = next_sunuke(n) + 1
