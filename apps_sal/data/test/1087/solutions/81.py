N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

less = -float('inf')
eq = 0

for d in range(60)[::-1]:
    mask = (1 << d)

    one = len([0 for a in A if (a & mask) != 0])
    zero = N - one

    l = less + mask * max(one, zero)

    if (K & mask) != 0:
        l = max(l, eq + mask * one)

    less = l
    eq += mask * (one if (K & mask == 0) else zero)

print((max(less, eq)))
