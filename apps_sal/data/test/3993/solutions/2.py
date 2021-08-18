n, m, k = list(map(int, input().split()))
P = [int(x) for x in input().split()]
P.reverse()

ops = 0
i = 1
while P:

    nxt = P[-1]
    togo = nxt - i
    skip = togo // k * k
    i += skip

    space = k
    while space:
        special = 0
        while P and P[-1] < i + space:
            special += 1
            P.pop()
        i += space
        if not special:
            break
        ops += 1
        space = special

print(ops)
