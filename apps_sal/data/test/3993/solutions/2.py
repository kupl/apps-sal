n,m,k = list(map(int,input().split()))
P = [int(x) for x in input().split()]
P.reverse()

# pages of size k
ops = 0
i = 1
while P:
    # while space left
    #   fill elements and count special
    #   remove special
    #   ops += 1

    # put elements in while not special

    # then onto next page

    nxt = P[-1]
    togo = nxt - i
    skip = togo//k*k
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

