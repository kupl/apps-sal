input()
colour = {'R': 0, 'G': 1, 'B': 2, 'Y': 3, 'W': 4}
cards = {(colour[c], ord(v) - ord('1')) for c, v in input().split()}


def ok(cs, vs):
    return len({
        (c if (cs >> c) & 1 else -1, v if (vs >> v) & 1 else -1)
        for c, v in cards
    }) == len(cards)


print((min(bin(cs).count('1') + bin(vs).count('1')
           for cs in range(1 << 5) for vs in range(1 << 5)
           if ok(cs, vs)
           )))
